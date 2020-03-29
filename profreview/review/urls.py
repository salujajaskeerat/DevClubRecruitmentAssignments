from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
#will be using the views module of user.
app_name='review'
urlpatterns=[
	url((r'^$'),views.IndexView.as_view(),name='index'),
	url(r'^(?P<pk>[0-9]+)/$',views.prof_details,name='details'),
	url(r'^dept/(?P<pk>[0-9]+)/$',views.prof_index,name='prof_details'),
	url((r'^register/$'),views.UserFormView.as_view(),name='register'),
	url((r'^login/$'),auth_views.LoginView.as_view(template_name='review/login.html'),name='Login'),
	url((r'^logout/$'),auth_views.LogoutView.as_view(template_name='review/logout.html'),name='Logout'),
	url(r'^profile/$',views.profile,name='profile' ),
	url(r'^(?P<pk>[0-9]+)/rating$',views.prof_rating,name='prof_rating'),

	# url for like/dislike of comments
	url(r'^(?P<pk>[0-9]+)/like_post$',views.like_post,name='like_post'),
	url(r'^search$',views.search,name='search')
	]