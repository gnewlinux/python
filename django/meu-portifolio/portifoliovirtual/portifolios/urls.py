from django.conf.urls import url
from . import views

urlpatterns = [
	url('^$', views.portifolio_exibir),
]