from django.conf.urls import url, include

urlpatterns = [
    url(r'^post/', include('post.urls.apis', namespace='post')),
    url(r'^member/', include('member.urls.apis', namespace='member')),
]
