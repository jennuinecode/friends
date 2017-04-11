from django.conf.urls import url
from . import views


app_name = "friends"

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^remove/(?P<id>\d+)$', views.remove, name="remove"),
	url(r'^add/(?P<id>\d+)$', views.add, name="add"),
	url(r'^view/(?P<id>\d+)$', views.view, name="view"),
]
