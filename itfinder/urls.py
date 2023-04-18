from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.i18n import set_language

urlpatterns = [
    path( 'admin/', admin.site.urls ),
    path( 'projects/', include( 'projects.urls' ) ),
    path( '', include( 'users.urls' ) ),
    path( 'set-language/', set_language, name='set_language' ),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
urlpatterns += static( settings.STATIC_URL, document_root=settings.STATIC_ROOT )
urlpatterns += i18n_patterns(
    path( '', include( 'users.urls' ) ), prefix_default_language=True
)
