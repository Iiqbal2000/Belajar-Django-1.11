from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^post/(?P<slugInput>[\w-]+)/$', views.slugPost, name="slug"),
    url(r'^kategori/(?P<kategoriInput>[\w-]+)/$', views.kategoriPost, name="kategori"),
]
