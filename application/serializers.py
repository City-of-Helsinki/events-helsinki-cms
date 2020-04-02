from rest_framework import serializers

from application import models


class CollectionsSerializer(serializers.ModelSerializer):
    title_en = serializers.CharField(source='title')
    curated_events = serializers.SerializerMethodField()

    class Meta:
        model = models.Collections
        exclude = ['title']

    def get_curated_events(self, obj):
        clean_curated_events = [curated_event.get('value') for curated_event in obj.curated_events.stream_data]
        return clean_curated_events


class LandingPageSerializer(serializers.ModelSerializer):
    title_en = serializers.CharField(source='title')

    class Meta:
        model = models.LandingPage
        exclude = ['title']
