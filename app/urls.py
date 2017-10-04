from django.conf.urls import include, url
from django.contrib import admin
from stories import views

from api import views as api_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/$', api_views.api_index),
    url(r'^api/stories/$', api_views.stories),
]
