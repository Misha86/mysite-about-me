from django.shortcuts import render_to_response, redirect, render
from django.contrib import auth
from django.core.context_processors import csrf
from loginsys.models import Profile
from loginsys.form import ProfileCreationForm
from django.contrib import messages


def login(request):
    args = {}
    path = request.META.get('HTTP_REFERER', '/')
    if path == request.build_absolute_uri():
        return_path = '/'
    else:
        return_path = path
    args['return_path'] = return_path
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
                auth.login(request, user)
                messages.success(request, 'Вітаю Вас на сайті, ' + username + '!', extra_tags='success')
                return redirect(return_path)
        elif not username and password:
            args['login_error_username'] = "Обов'язково введіть ім'я!"
            return render_to_response('login.html', args)
        elif username and not password:
            args['username'] = username
            args['login_error_password'] = "Обов'язково введіть пароль!"
            return render_to_response('login.html', args)
        elif not username and not password:
            args['login_error_username_password'] = "Ви не ввели жодних даних!"
            return render_to_response('login.html', args)
        else:
            args['login_error'] = 'Користувач не знайдений!'
            return render_to_response('login.html', args)
    else:
        return render(request, 'login.html', args)


def logout(request):
    messages.success(request, 'Щастливо, ' + request.user.username + '!', extra_tags='success')
    auth.logout(request)
    return_path = request.META.get('HTTP_REFERER', '/')  # HTTP_REFERER — ссылка на страницу с которой пришли на текущую, если такая существует
    return redirect(return_path)


def register(request):
    path = request.META.get('HTTP_REFERER', '/')
    if path == request.build_absolute_uri():
        return_path = '/'
    else:
        return_path = path
    form = ProfileCreationForm()
    if request.POST:
        form = ProfileCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            new_user = auth.authenticate(username=form.cleaned_data['username'],
                                         password=form.cleaned_data['password2'])
            new_profile = Profile(user=new_user, avatar=form.cleaned_data['avatar'],
                                  sex=form.cleaned_data['sex'])
            new_profile.save()
            auth.login(request, new_user)
            messages.success(request, 'Дякую, що долучилися до нас, ' + new_profile.user.username + '!',
                             extra_tags='success')
            return redirect(return_path)
        else:
            form = form
    context = {
        'form': form,
        'return_path': return_path,
    }
    return render(request, 'register.html', context)





