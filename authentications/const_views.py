
from rest_framework.authtoken import views 
from rest_framework import authentication, permissions
from rest_framework.response import Response

from . import const_models, const_serializers

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
        

class LocalAreaView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        object = const_models.LocalArea.objects.all()
        serializer = const_serializers.LocalAreaSerializer(object, many=True)
        return Response(serializer.data)
