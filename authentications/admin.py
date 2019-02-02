from django.contrib import admin
from .models import( 
    User, 
    ArtistProfile, 
    UserProfile, 
    RecordLabelProfile, 
    ManagementProfile
)
admin.site.register(User)
admin.site.register(ArtistProfile)
admin.site.register(UserProfile)
admin.site.register(RecordLabelProfile)
admin.site.register(ManagementProfile)
