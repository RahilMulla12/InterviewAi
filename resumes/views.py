from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Resume
from accounts.serializers import ResumeSerializer
from resumes.services.pdf_parser import extract_text_from_pdf
from resumes.services.gorq_service import extract_skills


class ResumeViewSet(viewsets.ModelViewSet):

    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user)

    def perform_create(self, serializer):

        resume = serializer.save(user=self.request.user)
        text = extract_text_from_pdf(resume.file.path)
        print("Extracted Text:", text[:200])
        skills = extract_skills(text)
        print(f" Extracted Skills  {skills}")
        resume.extracted_text = text
        resume.extracted_skills = skills

        resume.save()