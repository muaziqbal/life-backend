from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class RoleAssignment(models.Model):
    user = models.ForeignKey('auth_service.CustomUser', on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    tenant_id = models.CharField(max_length=100)

    class Meta:
        unique_together = ('user', 'role', 'tenant_id')
