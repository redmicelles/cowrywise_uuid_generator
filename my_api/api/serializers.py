from rest_framework import serializers
from my_api.models import Uuid

class UuidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uuid
        fields = ['uuid', 'time_created']