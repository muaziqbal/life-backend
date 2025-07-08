from django.db import models
from auth_service.models import CustomUser

class EduJobSubmission(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    job_id = models.IntegerField()
    answer = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='pending')  # pending, reviewed, completed
