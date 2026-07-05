from django.db import models
from django.conf import settings


class InterviewSession(models.Model):
    Level=(("Beginner","Beginner"),
    ("Intermidiate","Intermidiate"),
    ("Advance","Advance"))

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    level = models.CharField(max_length=50,choices=Level,default="Beginner")
    score = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.role


class InterviewQuestion(models.Model):

    session = models.ForeignKey(InterviewSession,related_name="questions",on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField(blank=True)
    feedback = models.TextField(blank=True)
    score = models.FloatField(default=0)

    def __str__(self):
        return self.question[:50]