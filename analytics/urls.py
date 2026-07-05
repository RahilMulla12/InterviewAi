from rest_framework.routers import DefaultRouter
from .views import UserAnalyticsViewSet

router = DefaultRouter()

router.register("analytics",UserAnalyticsViewSet,basename="analytics")
urlpatterns = router.urls