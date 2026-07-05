from rest_framework.routers import DefaultRouter
from .views import InterviewSessionViewSet,InterviewQuestionViewSet


router = DefaultRouter()

router.register("interviews",InterviewSessionViewSet,basename="interviews",)
router.register("questions",InterviewQuestionViewSet,basename="questions",)

urlpatterns = router.urls