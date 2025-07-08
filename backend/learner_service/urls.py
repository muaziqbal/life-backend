from django.urls import path
from .views import LearnerDashboardView

urlpatterns = [
    path('dashboard/', LearnerDashboardView.as_view(), name='learner-dashboard'),
]
