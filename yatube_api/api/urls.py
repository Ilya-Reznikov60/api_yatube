from rest_framework import routers

from django.urls import include, path

from api.views import GroupViewSet, PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet
)

urlpatterns = [
    path('', include(router.urls)),
]
