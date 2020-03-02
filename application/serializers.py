from rest_framework import serializers

from application import models


class CollectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Collections
        exclude = []
