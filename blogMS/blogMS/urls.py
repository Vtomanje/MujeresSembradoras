from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
# seo
from django.contrib.sitemaps.views import sitemap
from applications.home.sitemap import EntrySitemap, Sitemap

urlpatterns_main = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.home.urls')),   
    re_path('', include('applications.entrada.urls')),
    re_path('', include('applications.favoritos.urls')),
    # urls de terceros
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    
] 

if settings.DEBUG:
    urlpatterns_main += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns_main += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns_main += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]

# objeto site map que genera xml
sitemaps = {
    'site':Sitemap(
        [
            'home_app:index'
        ]
    ),
    'entradas': EntrySitemap
}
urlpatterns_sitemap = [
    path(
        'sitemap.xml', 
        sitemap, 
        {'sitemaps':sitemaps},
        name='django.contrib.sitemap.views.sitemap'
    )
]

urlpatterns = urlpatterns_main + urlpatterns_sitemap