from django.conf.urls import url
from loginsys.views import (login,
                            logout,
                            register)


urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^register/$', register, name='register'),
    ]

