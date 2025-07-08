from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from auth_service.models import CustomUser
from auth_service.permissions import IsLearner

class LearnerDashboardView(APIView):
    permission_classes = [IsAuthenticated and IsLearner]

    def get(self, request):
        user = request.user
        if user.role != 'learner':
            return Response({"error": "Forbidden"}, status=403)

        # Replace this with real DB data later
        data = {
            "full_name": user.full_name,
            "earnings": 120,
            "edu_jobs": [
                {"id": 1, "title": "Math Quiz", "status": "completed"},
                {"id": 2, "title": "Science Video", "status": "in_progress"},
                {"id": 3, "title": "Essay Writing", "status": "not_started"},
            ],
            "badges": ["Quiz Master", "Fast Learner"]
        }

        return Response(data)
