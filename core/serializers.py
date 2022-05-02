from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelViewSet, FlexFieldsModelSerializer

from core import models


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.State
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = '__all__'

    # expandable_fields = {
    #      'state': (
    #         'core.StateSerializer',
    #         {'source': 'state', 'fields': ['name', 'id']})
    # }
    def to_representation(self, obj):
        return {
            "id": obj.id,
            "name": obj.name,
            "created_at": obj.created_at,
            "modified_at": obj.modified_at,
            "active": obj.active,
            "state": obj.state.id,
            "state_name": obj.state.name
        }


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Zone
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.District
        fields = '__all__'

    def to_representation(self, obj):
        return {
            "id": obj.id,
            "name": obj.name,
            "created_at": obj.created_at,
            "modified_at": obj.modified_at,
            "active": obj.active,
            "zone": obj.city.id,
            "zone_name": obj.zone.name,
            "city": obj.city.id,
            "city_name": obj.city.name
        }