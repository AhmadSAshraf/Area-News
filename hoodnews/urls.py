from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^new/post$', views.new_post, name='newpost'),
    url(r'^hoods', views.all_hoods, name='hoods'),
    url(r'^business/',views.create_business,name = 'business'),
    url(r'^profile/(?P<user_id>\d+)?$', views.profile, name='profile'),
    url(r'^createHood/$', views.createHood, name='createHood'),
    url(r'^update/profile$', views.updateprofile, name='updateprofile'),
    url(r'^join/(\d+)', views.join, name='joinHood'),
   url(r'^search/$', views.search, name='search'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)