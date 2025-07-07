from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import send_push_notification, send_email

class NotifyView(APIView):
    def post(self, request):
        notif_type = request.data.get("type")
        to = request.data.get("to")
        subject = request.data.get("subject")
        message = request.data.get("message")

        if notif_type == "push":
            send_push_notification(to, subject, message)
        elif notif_type == "email":
            send_email(to, subject, message)
        else:
            return Response({"error": "Invalid type"}, status=400)

        return Response({"status": "sent"})
