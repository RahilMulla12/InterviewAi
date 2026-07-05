from rest_framework import serializers
from .models import User
from interviews.models import InterviewSession,InterviewQuestion
from resumes.models import Resume
from analytics.models import UserAnalytics


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True,min_length=8)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "role"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = [
            "password",
            "groups",
            "user_permissions"
             ]

class InterviewQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewQuestion
        fields = "__all__"


class InterviewSessionSerializer(serializers.ModelSerializer):

    questions = InterviewQuestionSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = InterviewSession
        fields = "__all__"
        read_only_fields = [
            "user",
            "status",
            "score",
            "role",
            "created_at",
        ]

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields="__all__"
        read_only_fields=(
            "user",
            "extracted_text",
            "extracted_skills",
            "uploaded_at"
        )


class UserAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnalytics
        fields = "__all__"