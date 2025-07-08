from django.urls import path
from .views import LearnerDashboardView
from .view.edu_jobs import EduJobDetailView 

urlpatterns = [
    path('dashboard/', LearnerDashboardView.as_view(), name='learner-dashboard'),
    path('jobs/<int:job_id>/', EduJobDetailView.as_view(), name='edu-job-detail'),
]
