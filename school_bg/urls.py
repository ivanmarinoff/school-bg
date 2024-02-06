"""
URL configuration for sova_school project.

"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('school_bg.web.urls')),
    # path('content/', include('school_bg.content.urls')),
    # path('users/', include('school_bg.users.urls')),
    # path('global_content/', include('school_bg.global_content.urls')),
    path('api/content/', include('school_bg.content.urls')),
    path('api/global_content/', include('school_bg.global_content.urls')),
    path('api/users/', include('school_bg.users.urls')),
    # path('schema/', include('schema_viewer.urls')),
]

if not settings.DEBUG:
    handler400 = 'school_bg.exception.bad_request'
    handler403 = 'school_bg.exception.permission_denied'
    handler500 = 'school_bg.exception.server_error'

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)