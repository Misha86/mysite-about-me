from django.conf.urls import url, include
from django.views.generic import TemplateView


app_name = 'blog'


urlpatterns = [
    # include urls_api
    url(r'^api/', include('blog.class_based.urls')),

    url(r'^$', 'blog.views.start_page', name='start_page'),
    url(r'^(?P<item_slug>.*)/(?P<category_slug>.*)/list/$', 'blog.views.article_list', name='article_list'),
    url(r'^(?P<item_slug>.*)/(?P<category_slug>.*)/list/update/$', 'blog.views.articles_list_update',
        name='articles_list_update'),
    url(r'^(?P<item_slug>.*)/(?P<category_slug>.*)/create/$', 'blog.views.article_create', name='article_create'),
    url(r'^(?P<item_slug>.*)/(?P<category_slug>.*)/(?P<article_slug>.*)/edit/$', 'blog.views.article_update',
        name='article_update'),
    url(r'^(?P<item_slug>.*)/(?P<category_slug>.*)/(?P<article_slug>.*)/delete/$', 'blog.views.article_delete',
        name='article_delete'),
    url(r'^(?P<item_slug>.*)/(?P<category_slug>.*)/(?P<article_slug>.*)/$', 'blog.views.article_detail',
        name='article_detail'),
    url(r'^(?P<item_slug>.*)/list/$', 'blog.views.photo', name='photo'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact_page.html')),
    url(r'^add_like/(?P<id>[0-9]+)/$', 'blog.views.add_like', name='add_like'),
    url(r'^3d-max/proposals/$', 'blog.views.proposals', name='proposals'),
    ]

