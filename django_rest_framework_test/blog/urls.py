from rest_framework import routers

from .views import EntryViewSet, UserViewSet


router = routers.DefaultRouter()
router.register("entries", EntryViewSet)
router.register("users", UserViewSet)
