import uuid
from rest_framework import response, status, permissions
from rest_framework.response import Response
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView
)

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet

# from rest_framework import authentication, permissions
from django.utils import timezone
from django.http import Http404
from django.utils.dateparse import parse_date
from dashboard.models import(
    # MusicPlayList,
    SongList,
    AlbumList,
    MusicPlayList,
    PlayListDetail,
    UserEarning
)
from authentications.models import (
    User,
    ArtistProfile,
    RecordLabelProfile,
    ManagementProfile
)

from dashboard.serializers import (
    # MusicReleaseSerializer,
    SongSerializer,
    AlbumSerializer,
    PlayListSerializer,
    PlayListDetailSerializer,
    UserEarningSerializer
)


class SongCreateAPIView(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = SongList.objects.all()
    serializer_class = SongSerializer
    parser_classes = (MultiPartParser, FormParser,)

    # def perform_create(self, serializer, format = None):
    #     serializer.save(owner=self.request.user,
    #     song = self.request.data.get('song')
    #     )

#         return response.Response(status=status.HTTP_202_ACCEPTED)


class SongListAPIView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    # queryset = SongList.objects.all()
    serializer_class = SongSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def get_queryset(self):
        qs = SongList.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(title_icontains=query)
        return qs


class SongDetailAPIView(RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = SongList.objects.all()
    serializer_class = SongSerializer
    parser_classes = (MultiPartParser, FormParser,)
    # lookup_field = 'id'


class SongUpdateAPIView(UpdateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = SongList.objects.all()
    serializer_class = SongSerializer
    parser_classes = (MultiPartParser, FormParser,)


class PlayListAPIViewSet(ModelViewSet):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PlayListSerializer,
    # default_user_space = None

    # def initial(self, request, *args, **kwargs):


class AlbumCreateAPIView(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = AlbumList.objects.all()
    serializer_class = AlbumSerializer
    parser_classes = (MultiPartParser, FormParser,)

class AlbumListAPIView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    # queryset = SongList.objects.all()
    serializer_class = AlbumSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def get_queryset(self):
        qs = AlbumList.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(title_icontains=query)
        return qs

class AlbumDetailAPIView(RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = AlbumList.objects.all()
    serializer_class = AlbumSerializer
    parser_classes = (MultiPartParser, FormParser,)