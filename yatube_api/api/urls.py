from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


router = DefaultRouter()

router.register(
    r"posts/(?P<post_id>[^/.]+)/comments",
    CommentViewSet, basename="comment"
)
router.register("posts", PostViewSet)
router.register("groups", GroupViewSet)
router.register("follow", FollowViewSet)

urlpatterns = [
    path('v1/jwt/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]
