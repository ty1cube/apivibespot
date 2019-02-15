from django.conf import settings
from django.contrib import admin
# from django.urls import url, include
# from django.conf.urls import  url
from django.urls import include, path

from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import AllowAny

if settings.DEBUG:
    import debug_toolbar

urlpatterns = [
    path('api/', include('authentications.urls')),

    path('api/v1/', include('dashboard.urls')),
    path('docs/', include_docs_urls(title='api documentation',
                                    permission_classes=(AllowAny,))),
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('__debug__/', include(debug_toolbar.urls)),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    # urlpatterns += [ url(r'^__debug__/', include(debug_toolbar.urls)),]

admin.site.site_header = "Vibespot Adminstrator"
admin.site.site_title = "Vibespot Adminstrator Portal"
admin.site.index_title = "Welcome to Vibespot Administrator Page"
