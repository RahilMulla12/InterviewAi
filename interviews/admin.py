from django.contrib import admin
from .models import InterviewSession,InterviewQuestion

# Register your models here.
admin.site.register(InterviewQuestion)
admin.site.register(InterviewSession)