from django.conf.urls import url
from .views import ArtikelList,ArtikelDetail,ArtikelUpdate,ArtikelDelete,ArtikelCreate

urlpatterns = [
    url(r'^$', ArtikelList.as_view(), name='index'),
    url(r'^search/$', ArtikelList.as_view(), name='search'),
    url(r'^detail/(?P<slug>[\w-]+$)', ArtikelDetail.as_view(), name='detail'),
    url(r'^create/$', ArtikelCreate.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)$',ArtikelUpdate.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)$', ArtikelDelete.as_view(), name='delete'),
]
