from django.db import models
from django.conf import settings


class UserAnalytics(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    total_interviews = models.IntegerField(default=0)
    average_score = models.FloatField(default=0)
    strongest_skill = models.CharField(max_length=100,blank=True)
    weakest_skill = models.CharField(max_length=100,blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username