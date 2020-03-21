from django.conf.urls import url
from . import views
app_name='review'
urlpatterns=[
	url((r'^$'),views.IndexView.as_view(),name='index'),
	url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='details'),
	url((r'^register/$'),views.UserFormView.as_view(),name='register'),
	url((r'^login/$'),views.Login.as_view(),name='Login'),
	]