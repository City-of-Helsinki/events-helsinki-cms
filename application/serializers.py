from rest_framework import serializers
from rest_framework.fields import CharField

from application import models
from project import settings


class CustomImageSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source="file.url")

    class Meta:
        model = models.CustomImage
        fields = ["url", "photographer_credit"]


def keywords_stream_field_serializer(keywords_field):
    clean_data = [field.get('value') for field in keywords_field.stream_data]
    return clean_data


class AboutPageSerializer(serializers.ModelSerializer):
    keywords_fi = serializers.SerializerMethodField()
    keywords_sv = serializers.SerializerMethodField()
    keywords_en = serializers.SerializerMethodField()

    def get_keywords_fi(self, obj):
        return keywords_stream_field_serializer(obj.keywords_fi)

    def get_keywords_sv(self, obj):
        return keywords_stream_field_serializer(obj.keywords_sv)

    def get_keywords_en(self, obj):
        return keywords_stream_field_serializer(obj.keywords_en)

    class Meta:
        fields = '__all__'
        model = models.AboutPage


class AccessibilityPageSerializer(serializers.ModelSerializer):
    keywords_fi = serializers.SerializerMethodField()
    keywords_sv = serializers.SerializerMethodField()
    keywords_en = serializers.SerializerMethodField()

    def get_keywords_fi(self, obj):
        return keywords_stream_field_serializer(obj.keywords_fi)

    def get_keywords_sv(self, obj):
        return keywords_stream_field_serializer(obj.keywords_sv)

    def get_keywords_en(self, obj):
        return keywords_stream_field_serializer(obj.keywords_en)

    class Meta:
        fields = '__all__'
        model = models.AccessibilityPage


class CollectionsSerializer(serializers.ModelSerializer):
    hero_image = CustomImageSerializer()
    curated_events = serializers.SerializerMethodField()

    keywords_fi = serializers.SerializerMethodField()
    keywords_sv = serializers.SerializerMethodField()
    keywords_en = serializers.SerializerMethodField()

    class Meta:
        model = models.Collections
        exclude = ['title']

    def get_curated_events(self, obj):
        clean_curated_events = [curated_event.get('value') for curated_event in
                                obj.curated_events.stream_data]
        return clean_curated_events

    def get_keywords_fi(self, obj):
        return keywords_stream_field_serializer(obj.keywords_fi)

    def get_keywords_sv(self, obj):
        return keywords_stream_field_serializer(obj.keywords_sv)

    def get_keywords_en(self, obj):
        return keywords_stream_field_serializer(obj.keywords_en)


class BannerPagesSerializer(serializers.ModelSerializer):
    hero_background_image = serializers.SerializerMethodField()

    hero_background_image_mobile = serializers.SerializerMethodField()

    hero_top_layer_image = serializers.SerializerMethodField()

    social_media_image = serializers.SerializerMethodField()

    title = serializers.SerializerMethodField()
    button_text = serializers.SerializerMethodField()
    button_url = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    title_and_description_color = serializers.SerializerMethodField()

    class Meta:
        model = models.BannerPages
        fields = ["hero_background_image",
                  "hero_background_image_mobile",
                  "hero_top_layer_image",
                  "social_media_image",
                  "button_text", "button_url", "title",
                  "description", "title_and_description_color"]

    def get_hero_background_image(self, obj):
        ret = {}
        for lang, _ in settings.LANGUAGES:
            ret[lang] = CustomImageSerializer(
                getattr(obj, f"hero_background_image_{lang}")).data
        return ret

    def get_hero_background_image_mobile(self, obj):
        ret = {}
        for lang, _ in settings.LANGUAGES:
            ret[lang] = CustomImageSerializer(
                getattr(obj, f"hero_background_image_mobile_{lang}")).data
        return ret

    def get_hero_top_layer_image(self, obj):
        ret = {}
        for lang, _ in settings.LANGUAGES:
            ret[lang] = CustomImageSerializer(
                getattr(obj, f"hero_top_layer_image_{lang}")).data
        return ret

    def get_social_media_image(self, obj):
        ret = {}
        for lang, _ in settings.LANGUAGES:
            ret[lang] = CustomImageSerializer(
                getattr(obj, f"social_media_image_{lang}")).data
        return ret

    def get_title(self, obj):
        ret = {}
        for lang, _ in settings.LANGUAGES:
            ret[lang] = getattr(obj, f"title_{lang}")
        return ret

    def get_button_text(self, obj):
        ret = {}
        for lang, _ in settings.LANGUAGES:
            ret[lang] = getattr(obj, f"button_text_{lang}")
        return ret

    def get_button_url(self, obj):
        ret = {}
        for lang, _ in settings.LANGUAGES:
            ret[lang] = getattr(obj, f"button_url_{lang}")
        return ret

    def get_description(self, obj):
        ret = {}
        for lang, _ in settings.LANGUAGES:
            ret[lang] = getattr(obj, f"description_{lang}")
        return ret

    def get_title_and_description_color(self, obj):
        ret = {}
        for lang, _ in settings.LANGUAGES:
            ret[lang] = getattr(obj, f"title_and_description_color_{lang}")
        return ret


class LandingPagesSerializer(serializers.ModelSerializer):
    top_banner = BannerPagesSerializer()
    bottom_banner = BannerPagesSerializer()
    keywords_fi = serializers.SerializerMethodField()
    keywords_sv = serializers.SerializerMethodField()
    keywords_en = serializers.SerializerMethodField()

    hero_background_image_fi = CustomImageSerializer()
    hero_background_image_sv = CustomImageSerializer()
    hero_background_image_en = CustomImageSerializer()

    hero_background_image_mobile_fi = CustomImageSerializer()
    hero_background_image_mobile_sv = CustomImageSerializer()
    hero_background_image_mobile_en = CustomImageSerializer()

    hero_top_layer_image_fi = CustomImageSerializer()
    hero_top_layer_image_sv = CustomImageSerializer()
    hero_top_layer_image_en = CustomImageSerializer()

    social_media_image_fi = CustomImageSerializer()
    social_media_image_sv = CustomImageSerializer()
    social_media_image_en = CustomImageSerializer()

    class Meta:
        model = models.LandingPages
        exclude = ['title']

    def get_keywords_fi(self, obj):
        return keywords_stream_field_serializer(obj.keywords_fi)

    def get_keywords_sv(self, obj):
        return keywords_stream_field_serializer(obj.keywords_sv)

    def get_keywords_en(self, obj):
        return keywords_stream_field_serializer(obj.keywords_en)
