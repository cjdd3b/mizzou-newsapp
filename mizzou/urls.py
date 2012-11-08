from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # More info on URL structures here:
    # https://docs.djangoproject.com/en/dev/topics/http/urls/

    ########## THE BASICS ##########

    # URL for static index view
    (r'^$', 'mizzou.apps.dispatch.views.dispatch_list'),
    # URL for statis detail view
    url(r'^(?P<slug>.*)/$', 'mizzou.apps.dispatch.views.dispatch_detail', name='dispatch_detail'),

    ########## ADVANCED ##########

    # URL for dynamic index view
    (r'^$', 'mizzou.apps.dispatch.views.index'),
    # URL for points JSON view
    (r'^points/', 'mizzou.apps.dispatch.views.map_api'),
)
