from django.urls import path
from .views import LearnerDashboardView
from .view.edu_jobs import EduJobDetailView, SubmitEduJobView

urlpatterns = [
    path('dashboard/', LearnerDashboardView.as_view(), name='learner-dashboard'),
    path('jobs/<int:job_id>/', EduJobDetailView.as_view(), name='edu-job-detail'),
    path('jobs/<int:job_id>/submit/', SubmitEduJobView.as_view(), name='edu-job-submit'),
]
