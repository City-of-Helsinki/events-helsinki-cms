from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from application import serializers
from application import models


class HealthCheck(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK)


class ReadinessCheck(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK)


class Collections(generics.ListAPIView):
    permission_classes = (AllowAny,)

    queryset = models.Collections.objects.all()
    serializer_class = serializers.CollectionsSerializer
    filterset_fields = ['visible_on_frontpage']


class CollectionsSingle(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)

    queryset = models.Collections.objects.all()
    serializer_class = serializers.CollectionsSerializer

    def get_object(self):
        draft_requested = self.request.query_params.get('draft') == 'true'

        collection_page = get_object_or_404(self.get_queryset(), pk=self.kwargs.get('pk'))

        if draft_requested:
            return collection_page.get_latest_revision_as_page()
        else:
            return collection_page


class LandingPages(generics.ListAPIView):
    permission_classes = (AllowAny,)

    queryset = models.LandingPages.objects.all()
    serializer_class = serializers.LandingPagesSerializer
    filterset_fields = ['visible_on_frontpage']
