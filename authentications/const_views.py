
from rest_framework.authtoken import views
from rest_framework import authentication, permissions
from rest_framework.response import Response
from authentications.const_models import State, LocalArea
from . import const_models, const_serializers
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView
)

class StateView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        object = State.objects.all()
        serializer = const_serializers.StateSerializer(object, many=True)
        return Response(serializer.data)


class LocalAreaView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        object = const_models.LocalArea.objects.all()
        # object = const_models.LocalArea.objects.filter(localareaview_set__state__id=id)
        # object = State.objects.filter(state=request.GET['state_id'])

        serializer = const_serializers.LocalAreaSerializer(object, many=True)
        return Response(serializer.data)

class LocalAreaDetailAPIView(RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = LocalArea.objects.all()
    serializer_class = const_serializers.LocalAreaSerializer
    