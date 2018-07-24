from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='list'),
    url(r'^create/$', views.post_create, name='create'),
    url(r'^detail/(?P<id>\d+)/$', views.post_detail, name='detail'),
    url(r'^update/$', views.post_detail, name='update'),
    url(r'^delete/$', views.post_detail, name='delete')
    # url(r'^$', views.post_home),
]
