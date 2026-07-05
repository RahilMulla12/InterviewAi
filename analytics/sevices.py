from django.db.models import Avg
from interviews.models import InterviewSession, InterviewQuestion
from .models import UserAnalytics


def update_user_analytics(user):
    analytics, created = UserAnalytics.objects.get_or_create(user=user)
    interviews = InterviewSession.objects.filter(user=user)
    questions = InterviewQuestion.objects.filter(session__user=user)
    analytics.total_interviews = interviews.count()
    analytics.total_questions = questions.count()
    analytics.average_score = (questions.aggregate(Avg("score"))["score__avg"] or 0)
    analytics.save()