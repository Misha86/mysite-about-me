from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', 'blog.views.start_page', name='start_page'),
    url(r'^create/$', 'blog.views.article_create', name='article_create'),
    url(r'^(?P<article_slug>.*)/edit/$', 'blog.views.article_update', name='article_update'),
    url(r'^(?P<article_slug>.*)/delete/$', 'blog.views.article_delete', name='article_delete'),
    url(r'^3d-max/(?P<category_slug>.*)/(?P<article_slug>.*)/$', 'blog.views.article_detail', name='article_detail'),
    url(r'^3d-max/(?P<category_slug>.*)/$', 'blog.views.article_list', name='article_list'),
    url(r'^photo/$', 'blog.views.photo', name='photo'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact_page.html')),
    url(r'^add_like/(?P<id>[0-9]+)/$', 'blog.views.add_like', name='add_like'),
    url(r'^3d-max/navigation-3d-max/$', 'blog.views.blog_3d_max', name='blog_3d_max'),
    url(r'^3d-max/proposals/$', 'blog.views.proposals', name='proposals'),
    ]

