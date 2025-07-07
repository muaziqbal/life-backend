from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#from django.contrib.auth.models import User
from .models import CustomUser as User
from rest_framework.permissions import AllowAny, IsAuthenticated

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, full_name="John Smith", role="learner", tenant_id="school_123")
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