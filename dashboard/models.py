import uuid
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from authentications.models import User
from authentications.const_models import (
    Country,
    State,
    LocalArea
)


# Create your models here.

# class BaseModel(models.Model):
#     # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     created_at = models.DateTimeField(default=timezone.now, editable=False)

# def upload_cover_image(instance, filename):
#     return "cover_image/{user}/{filename}".format(user=instance.user, filename=filename)

# def upload_song(instance, filename):
#     return "songs/{user}/{filename}".format(user=instance.user, filename=filename)


def upload_song_image(instance, filename):
    return "files/{user}/images/songs/{filename}".format(user=instance.user, filename=filename)


def upload_album_image(instance, filename):
    return "files/{user}/images/albums/{filename}".format(user=instance.user, filename=filename)


def upload_singles(instance, filename):
    return "files/{user}/songs/singles/{filename}".format(user=instance.user, filename=filename)


# def upload_album(instance, filename):
#     return "files/{user.unique_id}/songs/album/{filename}".format(unique_id=instance.user.unique_id, filename=filename)


class SongList(models.Model):
    user                     = models.ForeignKey('authentications.User', on_delete=models.CASCADE, blank=True, null=True)
    album                    = models.ForeignKey('dashboard.AlbumList', on_delete=models.CASCADE, blank=True, null=True)
    # music                    = models.ForeignKey('dashboard.MusicRelease', on_delete=models.CASCADE, blank=True, null=True)
    slug                       = models.SlugField(max_length=100, blank=True, null=True)
    title                     = models.CharField(max_length=100, blank=True, null=True)
    label_name                  = models.CharField(max_length = 100, blank=True, null=True)

    # email                       = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    genre                       = models.CharField(max_length=50, blank=True, null=True)
    country                     = models.ForeignKey("authentications.Country", on_delete=models.CASCADE, blank=True, null=True)
    # vibe_state                  = models.ForeignKey("authentications.State", on_delete=models.CASCADE, blank=True, null=True)
    push_state                  = models.ForeignKey("authentications.State", on_delete=models.CASCADE, blank=True, null=True)
    push_city                   = models.ForeignKey("authentications.LocalArea", on_delete=models.CASCADE, blank=True, null=True)
    release_date                = models.DateTimeField(auto_now_add=True)

    image                       = models.ImageField(upload_to=upload_song_image, blank=True, null=True)
    song                        =models.FileField(upload_to=upload_singles , blank=True, null=True)

    duration	                = models.CharField(max_length = 10, blank=True, null=True )	
    stream	                    = models.IntegerField(default = 0, blank=True, null=True) 
    streamed	                = models.IntegerField(default = 0,blank=True, null=True) 
    amount	                    = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    featured_artist             = models.CharField(max_length = 100, blank=True, null=True)
    contributors                = models.CharField(max_length = 100, blank=True, null=True)
    recording_year              = models.DateField(auto_now_add=True, blank=True, null=True)
    status	                    = models.BooleanField(True, blank=True, null=True)
    created_at                  = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'songs'

    def __str__(self):
        return self.title


class AlbumList(models.Model):
    user                        = models.ForeignKey('authentications.User', on_delete=models.CASCADE, blank=True, null=True)
    slug                        = models.SlugField(max_length=100, blank=True, null=True)
    title                       = models.CharField(max_length=100, blank=True, null=True)
    description                 = models.TextField(max_length=None, blank=True, null=True)
    image                       = models.ImageField(upload_to=upload_album_image, max_length=100,blank=True, null=True)
    year                        = models.CharField(max_length =100, blank=True, null=True)
    track_count                 = models.IntegerField(default = 0, blank=True, null=True)
    release_date                = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    status	                    = models.BooleanField(True, blank=True, null=True)
    created_at                  = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        db_table = 'albums'

    def __str__(self):
         return self.title

    

class MusicPlayList(models.Model):
    user                     = models.ForeignKey('authentications.User', on_delete=models.CASCADE)
    name                       = models.CharField(max_length=50)
    created_at                  = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'music_playlists'
    

class PlayListDetail(models.Model):
    user                     = models.ForeignKey('authentications.User', on_delete=models.CASCADE)
    playlist                  = models.ForeignKey('dashboard.MusicPlayList', on_delete=models.CASCADE)
    track                     = models.ForeignKey('dashboard.SongList', on_delete=models.CASCADE)
    created_at                  = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'music_playlists_details'
    
class UserEarning(models.Model):
    user                     = models.ForeignKey('authentications.User', on_delete=models.CASCADE)
    track                     = models.ForeignKey('dashboard.SongList', on_delete=models.CASCADE)
    earned_currency             = models.CharField(max_length=50)
    earned_amount               = models.DecimalField(max_digits=10, decimal_places=2)
    created_at                  = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_earning'

    # def __str__(self):
    #     return self.form_category