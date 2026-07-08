from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from interviews.models import InterviewSession, InterviewQuestion
from resumes.models import Resume


class DashboardViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]

    def list(self, request):

        user = request.user
        interviews = InterviewSession.objects.filter(user=user)
        resumes = Resume.objects.filter(user=user)
        questions = InterviewQuestion.objects.filter(session__user=user)

        total_interviews = interviews.count()
        total_resumes = resumes.count()

        total_score = sum(q.score for q in questions)
        total_questions = questions.count()

        average_score = (
            round(total_score / total_questions, 2)
            if total_questions > 0
            else 0
        )

        highest_score = (
            max((q.score for q in questions), default=0)
        )

        recent_interviews = interviews.order_by("-created_at")[:5]

        recent_data = []

        for interview in recent_interviews:

            recent_data.append(
                {
                    "id": interview.id,
                    "role": interview.role,
                    "level": interview.level,
                    "score": interview.score,
                    "created_at": interview.created_at,
                }
            )

        return Response(
            {
                "total_interviews": total_interviews,
                "total_resumes": total_resumes,
                "average_score": average_score,
                "highest_score": highest_score,
                "recent_interviews": recent_data,
            }
        )