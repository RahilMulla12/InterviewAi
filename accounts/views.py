from rest_framework import viewsets
from rest_framework.permissions import (AllowAny,IsAuthenticated)
from .models import User
from .serializers import (RegisterSerializer,UserSerializer)
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    def get_serializer_class(self):

        if self.action == "create":
            return RegisterSerializer

        return UserSerializer
    def get_permissions(self):

        if self.action == "create":
            return [AllowAny()]

        return [IsAuthenticated()]

    @action(detail=False, methods=["get"])
    def me(self, request):
     serializer = UserSerializer(request.user)
     return Response(serializer.data)