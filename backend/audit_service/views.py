from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
import pymongo

class AuditLogView(APIView):
    def get(self, request):
        client = pymongo.MongoClient(settings.MONGO_URI)
        logs = list(client[settings.MONGO_DB]["logs"].find().limit(100))
        for log in logs:
            log["_id"] = str(log["_id"])
        return Response(logs)
