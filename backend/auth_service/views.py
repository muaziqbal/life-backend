from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#from django.contrib.auth.models import User
from .models import CustomUser as User
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsOrgAdmin, IsLearner
from audit_service.utils import log_action
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, full_name="John Smith", role="learner", tenant_id="school_123")
        log_action(user.id, "register", {"username": user.username})
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email
        }) 
class OrgOnlyView(APIView):
    permission_classes = [IsOrgAdmin]

    def get(self, request):
        return Response({"message": "Hello Org Admin!"})

class LearnerOnlyView(APIView):
    permission_classes = [IsLearner]

    def get(self, request):
        return Response({"message": "Hello Org Learner!"})