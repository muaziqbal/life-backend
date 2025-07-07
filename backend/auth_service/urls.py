from django.urls import path
from .views import RegisterView, ProtectedView, OrgOnlyView, LearnerOnlyView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('me/', ProtectedView.as_view(), name='me'),
    path('org-only/', OrgOnlyView.as_view(), name='org-only'),
    path('learner-only/', LearnerOnlyView.as_view(), name='learner-only'),
]
