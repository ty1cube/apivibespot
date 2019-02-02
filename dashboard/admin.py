from django.contrib import admin
from .models import( 
    Track,
    PlayList,
    Album,
    PlayListDetail,
    UserEarning
)
admin.site.register(Track)
admin.site.register(PlayList)
admin.site.register(Album)
admin.site.register(PlayListDetail)
admin.site.register(UserEarning)


