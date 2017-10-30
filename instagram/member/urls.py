from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^profile/(?P<nickname>\w+)/$', views.profile, name='profile'),
    url(r'^facebook-login/$', views.facebook_login, name='facebook_login'),
    url(r'^follow/(?P<nickname>\w+)/$', views.follow, name='follow'),
]