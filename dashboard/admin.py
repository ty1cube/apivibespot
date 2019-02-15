from django.contrib import admin
from .models import( 
    SongList,
    MusicPlayList,
    AlbumList,
    PlayListDetail,
    UserEarning
)
admin.site.register(SongList)
admin.site.register(MusicPlayList)
admin.site.register(AlbumList)
admin.site.register(PlayListDetail)
admin.site.register(UserEarning)


