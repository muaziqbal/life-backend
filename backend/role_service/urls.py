from django.urls import path
from .views import RoleListView, AssignRoleView

urlpatterns = [
    path('list/', RoleListView.as_view(), name='role-list'),
    path('assign/', AssignRoleView.as_view(), name='role-assign'),
]
