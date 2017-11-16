from django.conf.urls import url, include

urlpatterns = [
    url(r'^post/', include('post.urls.apis', namespace='member')),
    url(r'^member/', include('member.urls.apis', namespace='post')),
]
