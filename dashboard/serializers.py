from rest_framework import serializers
from authentications.const_models import (
    State,
    LocalArea
)
from .models import(
    SongList,
    MusicPlayList,
    AlbumList,
    PlayListDetail,
    UserEarning
)
from rest_framework.reverse import reverse


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongList
        fields = "__all__"
        read_only_fields = ("created_at",)

    

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['state'].queryset = State.objects.none()

    # def create(self, validated_data):
    #     return TrackList.objects.create(**validated_data)



class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumList
        fields = "__all__"
        read_only_fields = ("created_at",)




class PlayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicPlayList
        fields = "__all__"
        read_only_fields = ("created_at",)



class PlayListDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayListDetail
        fields = "__all__"
        read_only_fields = ("created_at",)


class UserEarningSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEarning
        fields = "__all__"
        read_only_fields = ("created_at",)
