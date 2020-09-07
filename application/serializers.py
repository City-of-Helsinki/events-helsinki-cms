from rest_framework import serializers

from application import models


def image_serializer(image_field):
    if image_field:
        return {
            'url': image_field.file.url,
            'photographer_credit': image_field.photographer_credit,
        }
    else:
        return None


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
        return image_serializer(obj.hero_image)


class LandingPagesSerializer(serializers.ModelSerializer):
    hero_background_image_fi = serializers.SerializerMethodField()
    hero_background_image_sv = serializers.SerializerMethodField()
    hero_background_image_en = serializers.SerializerMethodField()

    hero_background_image_mobile_fi = serializers.SerializerMethodField()
    hero_background_image_mobile_sv = serializers.SerializerMethodField()
    hero_background_image_mobile_en = serializers.SerializerMethodField()

    hero_top_layer_image_fi = serializers.SerializerMethodField()
    hero_top_layer_image_sv = serializers.SerializerMethodField()
    hero_top_layer_image_en = serializers.SerializerMethodField()

    social_media_image_fi = serializers.SerializerMethodField()
    social_media_image_sv = serializers.SerializerMethodField()
    social_media_image_en = serializers.SerializerMethodField()

    class Meta:
        model = models.LandingPages
        exclude = ['title']

    def get_hero_background_image_fi(self, obj):
        return image_serializer(obj.hero_background_image_fi)

    def get_hero_background_image_sv(self, obj):
        return image_serializer(obj.hero_background_image_sv)

    def get_hero_background_image_en(self, obj):
        return image_serializer(obj.hero_background_image_en)

    def get_hero_background_image_mobile_fi(self, obj):
        return image_serializer(obj.hero_background_image_mobile_fi)

    def get_hero_background_image_mobile_sv(self, obj):
        return image_serializer(obj.hero_background_image_mobile_sv)

    def get_hero_background_image_mobile_en(self, obj):
        return image_serializer(obj.hero_background_image_mobile_en)

    def get_hero_top_layer_image_fi(self, obj):
        return image_serializer(obj.hero_top_layer_image_fi)

    def get_hero_top_layer_image_sv(self, obj):
        return image_serializer(obj.hero_top_layer_image_sv)

    def get_hero_top_layer_image_en(self, obj):
        return image_serializer(obj.hero_top_layer_image_en)

    def get_social_media_image_fi(self, obj):
        return image_serializer(obj.social_media_image_fi)

    def get_social_media_image_sv(self, obj):
        return image_serializer(obj.social_media_image_sv)

    def get_social_media_image_en(self, obj):
        return image_serializer(obj.social_media_image_en)
