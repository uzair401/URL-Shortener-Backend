from rest_framework import serializers
from .models import ShortUrl

class ShortURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortUrl
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'hit_count']