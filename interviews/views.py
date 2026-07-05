from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import InterviewSession, InterviewQuestion
from accounts.serializers import InterviewSessionSerializer,InterviewQuestionSerializer
from resumes.services.gorq_service import generate_interview_questions,evaluate_answer


class InterviewSessionViewSet(viewsets.ModelViewSet):
    serializer_class = InterviewSessionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return InterviewSession.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=["post"])
    def generate_questions(self, request, pk=None):
        interview = self.get_object()

        skills = request.data.get("skills", [])

        questions = generate_interview_questions(
            interview.role,
            interview.level,
            skills,
        )

        created = []

        for item in questions:
            q = InterviewQuestion.objects.create(
                session=interview,
                question=item["question"],
            )

            created.append(
                InterviewQuestionSerializer(q).data
            )

        return Response(created)


class InterviewQuestionViewSet(viewsets.ModelViewSet):
    serializer_class = InterviewQuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return InterviewQuestion.objects.filter(
            session__user=self.request.user
        )

    @action(detail=True, methods=["post"])
    def submit_answer(self, request, pk=None):
     question = self.get_object()

     answer = request.data.get("answer")

     result = evaluate_answer(
        question.question,
        answer,
     )

     question.answer = answer
     question.score = result["score"]
     question.feedback = result["feedback"]

     question.save()

     return Response(
        InterviewQuestionSerializer(question).data
        )