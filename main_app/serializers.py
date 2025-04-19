from rest_framework import serializers
from .models import ShortURL

class ShortURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = '__all__'
        read_only_fields = ['short_url', 'created_at', 'updated_at', 'hit_count']