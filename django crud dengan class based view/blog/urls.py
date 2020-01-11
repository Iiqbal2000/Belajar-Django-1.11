from django.conf.urls import url
from .views import ArticleIndexView,ArticleDeleteView,ArticleCreateView

urlpatterns = [
    url(r'^$', ArticleIndexView.as_view(), name="index"),
    url(r'^delete/(?P<delete_id>[0-9]+)$', ArticleDeleteView.as_view(), name="delete"),
    url(r'^update/(?P<update_id>[0-9]+)$', ArticleCreateView.as_view(mode='update'), name="update"),
    url(r'^create/$', ArticleCreateView.as_view(), name="create"),
]
