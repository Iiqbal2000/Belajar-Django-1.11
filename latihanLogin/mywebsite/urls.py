from django.conf.urls import url
from django.contrib import admin
from .views import homeView,loginView,signupView,profil,logoutView


urlpatterns = [
    url(r'^profil/$', profil, name='profil'),
    url(r'^logout/$', logoutView, name='logout'),
    url(r'^signup/$', signupView, name='signup'),
    url(r'^login/$', loginView, name='login'),
    url(r'^$', homeView, name='home'),
    url(r'^admin/', admin.site.urls),
]
