from rest_flex_fields import FlexFieldsModelViewSet
from rest_framework import viewsets, filters

from core import models, serializers


class StateViewSet(viewsets.ModelViewSet):
    queryset = models.State.objects.all()
    serializer_class = serializers.StateSerializer
    ordering_fields = '__all__'
    ordering = ('-id',)


class CityViewSet(viewsets.ModelViewSet):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer
    ordering_fields = '__all__'
    ordering = ('-id',)


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = models.Zone.objects.all()
    serializer_class = serializers.ZoneSerializer


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = models.District.objects.all()
    serializer_class = serializers.DistrictSerializer
    ordering_fields = '__all__'
    ordering = ('-id',)
