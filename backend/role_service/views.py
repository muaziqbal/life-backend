from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Role, RoleAssignment
from .serializers import RoleSerializer, RoleAssignmentSerializer
from rest_framework.permissions import IsAuthenticated

class RoleListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)

class AssignRoleView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = RoleAssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
