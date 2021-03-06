from django.conf.urls import patterns, include, url
# for statci()
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^app/', include('app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # contents
    url(r'^news/page/(?P<page>.+).html$','app.contents.views.news_page', name='contents_news_page',),
    url(r'^news/(?P<id>.+).html$','app.contents.views.news_item', name='contents_news_item',),
    url(r'^(?P<path>.+).html$','app.contents.views.render', name='contents_render',),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
