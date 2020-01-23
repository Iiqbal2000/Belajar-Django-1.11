from django.conf.urls import url
from django.contrib import admin
from .views import index,LoginViewCbv,profil,LogoutViewCbv,RegisterViewCbv

urlpatterns = [
    url(r'^signup/$', RegisterViewCbv.as_view(), name='signup'),
    url(r'^logout/$', LogoutViewCbv.as_view(), name='logout'),
    url(r'^profil/$', profil, name='profil'),
    url(r'^login/$', LoginViewCbv.as_view(), name='login'),
    url(r'^$', index, name='index'),
    url(r'^admin/', admin.site.urls),
]
