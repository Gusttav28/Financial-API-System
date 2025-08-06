from rest_framework import serializers
from database.models import Item

class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"