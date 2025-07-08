from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from auth_service.models import CustomUser
from auth_service.permissions import IsLearner
from learner_service.models import EduJobSubmission
from learner_service.serializers import EduJobSubmissionSerializer

class EduJobDetailView(APIView):
    permission_classes = [IsAuthenticated, IsLearner]

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

class SubmitEduJobView(APIView):
    permission_classes = [IsAuthenticated, IsLearner]

    def post(self, request, job_id):
        data = request.data.copy()
        #data['user'] = request.user.id
        data['job_id'] = job_id
        print(data)
        serializer = EduJobSubmissionSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response({"message": "Submission received!"}, status=201)
        return Response(serializer.errors, status=400)