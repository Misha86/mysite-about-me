from django.conf.urls import url


urlpatterns = [
    url(r'^(?P<lang_code>.*)/$', 'languages.views.set_language', name='set_language'),
    ]

