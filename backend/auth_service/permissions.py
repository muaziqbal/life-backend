from rest_framework.permissions import BasePermission

class IsOrgAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'org_admin'

class IsLearner(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'learner'

class IsContentCreator(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'content_creator'
