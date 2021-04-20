from rest_framework import serializers
from .models import Page

class PagesSerializer(serializers.Serializer):
    class Meta:
        model = Page
        fields = "__all__"
