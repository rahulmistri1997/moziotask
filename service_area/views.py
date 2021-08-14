from django.shortcuts import render
from django.contrib.gis.geos import Point

from rest_framework import viewsets, status

from service_area.serializers import ProviderSerializer, ServiceAreaSerializer
from service_area.models import Provider, ServiceArea
from rest_framework.response import Response


class ProviderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows providers to be created, viewed or edited.
    GET -> Get list of all Providers . GET/{id} -> Get detail of Provider
    POST -> Create Provider
    PUT -> Update Provider
    DELETE -> Delete Provider
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ServiceAreaViewSet(viewsets.ModelViewSet):
    """
    GET -> Get list of all ServiceAreas . GET/{id} -> Get detail of ServiceArea
    POST -> Create ServiceArea
    PUT -> Update ServiceArea
    DELETE -> Delete ServiceArea

    If QueryParam {
        lat: defaultValue = None
        lng: defaultValue = None
    } -> Search areas by taking lat & lng Params
    """
    serializer_class = ServiceAreaSerializer

    def get_queryset(self):
        queryset = ServiceArea.objects.all()

        lat = self.request.query_params.get('lat', None)
        lng = self.request.query_params.get('lng', None)

        if lat != None and lng != None:
            try:
                lat = float(lat)
                lng = float(lng)
                geopoint = Point(lat, lng)
                queryset = queryset.filter(area__intersects=geopoint)
            except Exception as e:
                pass

        return queryset
