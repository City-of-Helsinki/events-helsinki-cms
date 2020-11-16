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
    hero_image = serializers.SerializerMethodField()
    curated_events = serializers.SerializerMethodField()

    keywords_fi = serializers.SerializerMethodField()
    keywords_sv = serializers.SerializerMethodField()
    keywords_en = serializers.SerializerMethodField()

    class Meta:
        model = models.Collections
        exclude = ['title']

    def get_curated_events(self, obj):
        clean_curated_events = [curated_event.get('value') for curated_event in obj.curated_events.stream_data]
        return clean_curated_events

    def get_hero_image(self, obj):
        return image_serializer(obj.hero_image)

    def get_keywords_fi(self, obj):
        return keywords_stream_field_serializer(obj.keywords_fi)

    def get_keywords_sv(self, obj):
        return keywords_stream_field_serializer(obj.keywords_sv)

    def get_keywords_en(self, obj):
        return keywords_stream_field_serializer(obj.keywords_en)


class BannerPagesSerializer(serializers.ModelSerializer):
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

    class Meta:
        model = models.BannerPages
        fields = [
            "hero_background_image_fi", "hero_background_image_sv", "hero_background_image_en",
            "hero_background_image_mobile_fi", "hero_background_image_mobile_en", "hero_background_image_mobile_sv",
            "hero_top_layer_image_fi", "hero_top_layer_image_sv", "hero_top_layer_image_en",
            "social_media_image_fi", "social_media_image_en", "social_media_image_sv",
            "button_text_fi", "button_text_en", "button_text_sv",
            "button_url_fi", "button_url_sv", "button_url_en",
            "title_fi", "title_sv", "title_en",
            "description_fi", "description_en", "description_sv"
        ]


class LandingPagesSerializer(serializers.ModelSerializer):
    top_banner = BannerPagesSerializer()
    bottom_banner = BannerPagesSerializer()
    keywords_fi = serializers.SerializerMethodField()
    keywords_sv = serializers.SerializerMethodField()
    keywords_en = serializers.SerializerMethodField()

    class Meta:
        model = models.LandingPages
        exclude = ['title']

    def get_keywords_fi(self, obj):
        return keywords_stream_field_serializer(obj.keywords_fi)

    def get_keywords_sv(self, obj):
        return keywords_stream_field_serializer(obj.keywords_sv)

    def get_keywords_en(self, obj):
        return keywords_stream_field_serializer(obj.keywords_en)
