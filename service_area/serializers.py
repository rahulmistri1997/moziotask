from rest_framework import serializers

from service_area.models import Provider, ServiceArea


class ProviderSerializer(serializers.ModelSerializer):
    """ Serializers for Provider Model """
    
    class Meta:
        model = Provider
        fields = '__all__' #__all__ is used to include all fields in the serializer


class ServiceAreaSerializer(serializers.ModelSerializer):
    """ Serializers for ServiceArea Model """

    provider_name = serializers.SerializerMethodField()

    class Meta:
        model = ServiceArea
        fields = '__all__'

    def get_provider_name(self, obj):
        return obj.provider.name