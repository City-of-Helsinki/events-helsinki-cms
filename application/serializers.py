from rest_framework import serializers

from application import models


class CollectionsSerializer(serializers.ModelSerializer):
    hero_image = serializers.SerializerMethodField()
    curated_events = serializers.SerializerMethodField()

    class Meta:
        model = models.Collections
        exclude = ['title']

    def get_curated_events(self, obj):
        clean_curated_events = [curated_event.get('value') for curated_event in obj.curated_events.stream_data]
        return clean_curated_events

    def get_hero_image(self, obj):
        if obj.hero_image:
            return obj.hero_image.file.url
        else:
            return None


class LandingPagesSerializer(serializers.ModelSerializer):
    hero_background_image_fi = serializers.SerializerMethodField()
    hero_background_image_sv = serializers.SerializerMethodField()
    hero_background_image_en = serializers.SerializerMethodField()

    hero_top_layer_image_fi = serializers.SerializerMethodField()
    hero_top_layer_image_sv = serializers.SerializerMethodField()
    hero_top_layer_image_en = serializers.SerializerMethodField()

    class Meta:
        model = models.LandingPages
        exclude = ['title']

    def get_hero_background_image_fi(self, obj):
        if obj.hero_background_image_fi:
            return obj.hero_background_image_fi.file.url
        else:
            return None

    def get_hero_background_image_sv(self, obj):
        if obj.hero_background_image_sv:
            return obj.hero_background_image_sv.file.url
        else:
            return None

    def get_hero_background_image_en(self, obj):
        if obj.hero_background_image_en:
            return obj.hero_background_image_en.file.url
        else:
            return None

    def get_hero_top_layer_image_fi(self, obj):
        if obj.hero_top_layer_image_fi:
            return obj.hero_top_layer_image_fi.file.url
        else:
            return None

    def get_hero_top_layer_image_sv(self, obj):
        if obj.hero_top_layer_image_sv:
            return obj.hero_top_layer_image_sv.file.url
        else:
            return None

    def get_hero_top_layer_image_en(self, obj):
        if obj.hero_top_layer_image_en:
            return obj.hero_top_layer_image_en.file.url
        else:
            return None
