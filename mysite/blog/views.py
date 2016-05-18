from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from blog.models import Article
from navigation.models import Category
from blog.form import SendMassageForm, ArticleForm
from comment.forms import CommentForm
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import gettext as _
from loginsys.models import Profile
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def start_page(request):
    form = SendMassageForm()
    users = Profile.objects.exclude(pk=request.user.pk).order_by('-user__date_joined')
    current_page = Paginator(users, 6)
    page_number = request.GET.get('page', 1)
    users_list = current_page.page(page_number)
    if request.POST and 'pause' not in request.session:
        form = SendMassageForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            massage = form.cleaned_data['massage']
            send_mail(email, massage, email, [settings.EMAIL_HOST_USER],)
            request.session.set_expiry(60)
            request.session['pause'] = True
            return redirect('/')
    context = {
        'form': form,
        'users': users_list,
        }
    return render(request, 'content_start_page.html', context)


def article_create(request):
    if not request.user.is_superuser:
        raise Http404
    title = 'Форма для створення статті'
    button_create = 'створити статтю'
    button_cancel = 'відміна'
    return_path = '/'
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.article_user = get_object_or_404(Profile, user=request.user)
        instance.save()
        messages.success(request, "Ура, стаття сворена!", extra_tags='success')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'title': title,
        'button_create': button_create,
        'button_cancel': button_cancel,
        'form': form,
        'return_path': return_path,
        }
    return render(request, 'article_form.html', context)


def article_update(request, article_slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        # response = HttpResponse('<h1>Ти не маєш прав для оновлення статті!!!</h1')
        # response.status_code = 403
        # return response
        raise Http404
    title = 'Форма оновлення статті'
    button_create = 'змінити статтю'
    button_cancel = 'відміна'
    instance = get_object_or_404(Article, article_slug=article_slug)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Ура, стаття оновлена!", extra_tags='success')
        return HttpResponseRedirect(instance.get_absolute_url())
    return_path = instance.get_absolute_url()
    context = {
        'title': title,
        'button_create': button_create,
        'button_cancel': button_cancel,
        'return_path': return_path,
        'form': form,
        'article': instance,
        }
    return render(request, 'article_form.html', context)


def article_delete(request, article_slug=None):
    title = 'Ви впевнені, що хочете видалити дану статтю?'
    button_delete = 'видалити статтю'
    button_cancel = 'відміна'
    instance = get_object_or_404(Article, article_slug=article_slug)
    return_path = instance.get_absolute_url()
    context = {
        'title': title,
        'button_delete': button_delete,
        'button_cancel': button_cancel,
        'return_path': return_path,
        }
    if request.POST:
        instance.delete()
        messages.error(request, 'Стаття ' + '\'' + instance.article_title + '\'' + ' видалена!', extra_tags='success')
        return redirect('blog:article_list', category_slug=instance.article_category.category_name)
    return render(request, 'article_delete_form.html', context)


def article_list(request, category_slug):
    category_3d_max = get_object_or_404(Category, category_name=category_slug)
    articles_list = category_3d_max.articles.all().order_by('-article_date')
    articles_carousel = category_3d_max.articles.all().order_by('-article_likes')[0:3]
    query = request.GET.get('q')
    if query:
        articles_list = Article.objects.filter(
            Q(article_title__icontains=query) |
            Q(article_text__icontains=query)).distinct()
    paginator = Paginator(articles_list, 9)
    page = request.GET.get('page')
    try:
        # it`s for pagination in bootstrap part 1
        page_before = int(page) - 3
        page_after = int(page) + 3
        list_pagination = []
        for p in paginator.page_range:
            if p == page or p == paginator.page_range[0] or p == paginator.page_range[-1]:
                list_pagination.append(p)
            elif p < page_before or p > page_after:
                if page_before == paginator.page_range[0]:
                    page_before += 1
                elif page_after == paginator.page_range[-1]:
                    page_after += 1
                else:
                    continue
            else:
                list_pagination.append(p)
        #
        articles = paginator.page(page)
    except PageNotAnInteger:
        article = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    # it`s for pagination in bootstrap: catch except TypeError part 2
    except TypeError:
        list_pagination = []
        for s in paginator.page_range:
            if s in paginator.page_range[:8] or s in paginator.page_range[-1:]:
                list_pagination.append(s)
                page_after = 8
            else:
                continue
        articles = paginator.page(1)
    return render(request, 'gallery_works.html', locals())


def article_detail(request, article_slug, category_slug):
    category_3d_max = get_object_or_404(Category, category_name=category_slug)
    article = category_3d_max.articles.get(article_slug=article_slug)
    comments = article.comments.all().order_by('-comments_create')
    current_page = Paginator(comments, 4)
    page_number = request.GET.get('page', 1)
    form = CommentForm(auto_id='id_for_%s', label_suffix=' -> -> -> ->')
    if request.POST and 'pause' in request.session:
        messages.error(request, 'Ви вже залишили коментар, зачекайте хвилину.', extra_tags='error')
    elif request.POST and 'pause' not in request.session:
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(article_slug=article_slug)
            comment.comments_user = Profile.objects.get(pk=request.user.pk)                            # АБО comment.comments_from = auth.get_user(request)  АБО comment.comments_from_id = auth.get_user(request).id
            comment.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
            messages.success(request, 'Коментар добавлений успішно!', extra_tags='success')
            return redirect(article.get_absolute_url())
    context = {
        'comments': current_page.page(page_number),
        'article': article,
        'form': form,
        }
    return render(request, 'gallery_work.html', context)


def add_like(request, id=None):
    try:
        if id in request.COOKIES:
            return_path = request.META.get('HTTP_REFERER', '/')
            return redirect(return_path)
        else:
            article = Article.objects.get(id=id)
            article.article_likes += 1
            article.save()
            redirect_path = request.META.get('HTTP_REFERER', '/')
            response = redirect(redirect_path)
            response.set_cookie(id, 'test')
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')


def blog_3d_max(request):
    blog_3d_max = {}
    return render(request, 'blog_3d_max.html', blog_3d_max)


def proposals(request):
    pass


def photo(request):
    pass


def django_python(request):
    pass


def html_5(request):
    pass


def css_3(request):
    pass


def bootstrap(request):
    pass

