from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheck(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK)


class ReadinessCheck(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK)


class Collections(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK)
