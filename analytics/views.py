from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.serializers import UserAnalyticsSerializer
from .models import UserAnalytics


class UserAnalyticsViewSet(viewsets.ModelViewSet):
    serializer_class=UserAnalyticsSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return UserAnalytics.objects.filter(user=self.request.user)

