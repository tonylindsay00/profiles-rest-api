from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serialises the name feils to test out API view"""
    name =  serializers.CharField(max_length=10)
