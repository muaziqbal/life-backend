from django.db import models

class Notification(models.Model):
    NOTIF_TYPE = (("email", "Email"), ("push", "Push"))

    recipient = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    type = models.CharField(max_length=10, choices=NOTIF_TYPE)
    status = models.CharField(max_length=50, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
