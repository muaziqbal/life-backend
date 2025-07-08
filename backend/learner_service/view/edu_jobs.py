from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from auth_service.models import CustomUser
from auth_service.permissions import IsLearner

class EduJobDetailView(APIView):
    permission_classes = [IsAuthenticated and IsLearner]

    def get(self, request, job_id):
        user = request.user
        if user.role != 'learner':
            return Response({"error": "Forbidden"}, status=403)

        # Mock data — replace with real DB fetch later
        data = {
            "id": job_id,
            "title": "Essay Writing",
            "description": "Write an essay about your favorite animal.",
            "type": "written",
            "status": "not_started",
            "resources": [
                { "type": "pdf", "url": "https://example.com/essay-guide.pdf" },
                { "type": "video", "url": "https://example.com/essay-video.mp4" }
            ]
        }

        return Response(data)
