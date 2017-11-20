from django.conf.urls import url
from django.conf.urls.static import static

from django.conf import settings

from . import views


urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^post/(\d+)$', views.post, name='post'),
    url(r'^tag/(\d+)$', views.tag, name='tag'),
    url(r'^about/', views.about, name='about'),
    url(r'^explore/', views.explore, name='explore'),
    url(r'^collections/', views.collections, name='collections'),

]


if settings.DEBUG:

    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)