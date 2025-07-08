from rest_framework import serializers
from .models import EduJobSubmission

class EduJobSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EduJobSubmission
        fields = '__all__'
        read_only_fields = ['user', 'submitted_at']
