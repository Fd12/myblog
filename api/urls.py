from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.PostListView.as_view(),  name="list"),
    url(r'^create/$', views.PostCreateView.as_view(),  name="create"),
    url(r'^(?P<post_slug>[-\w]+)/detail/$', views.PostDetailView.as_view(),  name="detail"),
    url(r'^(?P<post_slug>[-\w]+)/delete/$', views.PostDeleteView.as_view(),  name="delete"),
    url(r'^(?P<post_slug>[-\w]+)/update/$', views.PostUpdateView.as_view(),  name="update"),
    url(r'^comments/$', views.CommentListView.as_view(),  name="comment-list"),
   	url(r'^comments/create$', views.CommentCreateView.as_view(),  name="comment-create"),
   	url(r'^register/$', views.UserCreateView.as_view(),  name="register"),
   	url(r'^login/$', views.UserLoginView.as_view(),  name="login"),
]