
from rest_framework.authtoken import views
from rest_framework import authentication, permissions
from rest_framework.response import Response

from . import const_models, const_serializers
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView
)

class CountryView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        object = const_models.Country.objects.all()
        serializer = const_serializers.CountrySerializer(object, many=True)
        return Response(serializer.data)


class StateView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        object = const_models.State.objects.all()
        serializer = const_serializers.StateSerializer(object, many=True)
        return Response(serializer.data)

class StateDetailAPIView(RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = const_models.State.objects.all()
    serializer_class = const_serializers.StateSerializer
    

class LocalAreaView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        object = const_models.LocalArea.objects.all()
        serializer = const_serializers.LocalAreaSerializer(object, many=True)
        return Response(serializer.data)

class LocalAreaDetailAPIView(RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = const_models.LocalArea.objects.all()
    serializer_class = const_serializers.LocalAreaSerializer
    