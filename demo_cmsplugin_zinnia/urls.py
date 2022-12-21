"""Urls for the cmsplugin_zinnia demo"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from django.urls import path
from django.contrib.sitemaps.views import index, sitemap
from django.views.defaults import page_not_found, bad_request, permission_denied, server_error
from django.views.static import serve

from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap

admin.autodiscover()

urlpatterns = [
    path('blog/', include('zinnia.urls', namespace='zinnia')),
    path('comments/', include('django_comments.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
]

sitemaps = {
    'tags': TagSitemap,
    'blog': EntrySitemap,
    'authors': AuthorSitemap,
    'categories': CategorySitemap
}

urlpatterns += [
    path('sitemap.xml', index, {'sitemaps': sitemaps}),
    path('sitemap-<str:section>.xml', sitemap, {'sitemaps': sitemaps}),
]

urlpatterns += [
    path('400/', bad_request),
    path('403/', permission_denied),
    path('404/', page_not_found),
    path('500/', server_error),
]

if settings.DEBUG:
    urlpatterns += [
        path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT})
    ]

urlpatterns += [
    path('', include('cms.urls')),
]
