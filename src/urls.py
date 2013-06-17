from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.conf.urls.static import static
from django.contrib import admin
from mes_fichiers.views import TinymceView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TinymceView.as_view()),
    url(r'^mes_fichiers/', include('mes_fichiers.urls',
                                   namespace='mes_fichiers')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)