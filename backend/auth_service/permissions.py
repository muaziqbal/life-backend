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

class IsSameTenant(BasePermission):
    def has_permission(self, request, view):
        target_tenant = request.query_params.get('tenant_id') or request.data.get('tenant_id')
        return (
            request.user.is_authenticated and
            request.user.tenant_id and
            request.user.tenant_id == target_tenant
        )

class IsTenantCoach(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == "coach" and
            request.user.tenant_id == request.query_params.get('tenant_id')
        )
