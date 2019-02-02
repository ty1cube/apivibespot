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

def upload_cover_image(instance, filename):
    return "cover_image/{user}/{filename}".format(user=instance.user, filename=filename)


def upload_song(instance, filename):
    return "songs/{user}/{filename}".format(user=instance.user, filename=filename)


class Track(models.Model):
    user                     = models.ForeignKey('authentications.User', on_delete=models.CASCADE)
    album_id                    = models.ForeignKey('dashboard.Album', on_delete=models.CASCADE)
    slug                        = models.SlugField(max_length=100)
    title                       = models.CharField(max_length=100)
    description                 = models.TextField(max_length=None)
    label_name                  = models.CharField(max_length = 100)
    email                       = models.EmailField(max_length=100, unique=True)
    genre                       = models.CharField(max_length=50)
    country                     = models.ForeignKey("authentications.Country", on_delete=models.CASCADE, blank=True, null=True)
    # vibe_state                  = models.ForeignKey("authentications.State", on_delete=models.CASCADE, blank=True, null=True)
    push_state                  = models.ForeignKey("authentications.State", on_delete=models.CASCADE, blank=True, null=True)
    push_city                   = models.ForeignKey("authentications.LocalArea", on_delete=models.CASCADE, blank=True, null=True)
    release_date                = models.DateTimeField(auto_now_add=True)
    image                       = models.ImageField(upload_to=upload_cover_image, blank=True, null=True)
    song                        =models.FileField(upload_to=upload_song, blank=True, null=True)
    duration	                = models.CharField(max_length = 10 )	
    stream	                    = models.IntegerField(11) 
    streamed	                = models.IntegerField(11) 
    amount	                    = models.IntegerField(11) 
    featured_artist             = models.CharField(max_length = 100)
    contributors                = models.CharField(max_length = 100)
    recording_year              = models.CharField(max_length =100)
    status	                    = models.BooleanField(True)
    created_at                  = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tracks'


class Album(models.Model):
    user_id                     = models.ForeignKey('authentications.User', on_delete=models.CASCADE)
    slug                        = models.SlugField(max_length=100)
    title                       = models.CharField(max_length=100)
    description                 = models.TextField(max_length=None)
    image                       = models.ImageField(upload_to=None, max_length=100,blank=True, null=True)
    year                        = models.CharField(max_length =100)
    track_count                 = models.IntegerField(11)
    release_date                = models.DateTimeField(auto_now_add=True)
    status	                    = models.BooleanField(True)
    created_at                  = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        db_table = 'albums'
    

class PlayList(models.Model):
    user_id                     = models.ForeignKey('authentications.User', on_delete=models.CASCADE)
    name                       = models.CharField(max_length=50)
    created_at                  = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'music_playlists'
    

class PlayListDetail(models.Model):
    user_id                     = models.ForeignKey('authentications.User', on_delete=models.CASCADE)
    playlist_id                  = models.ForeignKey('dashboard.PlayList', on_delete=models.CASCADE)
    track_id                     = models.ForeignKey('dashboard.Track', on_delete=models.CASCADE)
    created_at                  = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'music_playlists_details'
    
class UserEarning(models.Model):
    user_id                     = models.ForeignKey('authentications.User', on_delete=models.CASCADE)
    track_id                     = models.ForeignKey('dashboard.Track', on_delete=models.CASCADE)
    earned_currency             = models.CharField(max_length=50)
    earned_amount               = models.DecimalField(max_digits=10, decimal_places=2)
    created_at                  = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_earning'

    # def __str__(self):
    #     return self.form_category