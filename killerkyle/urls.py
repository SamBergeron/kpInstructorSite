from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import homePage
admin.autodiscover()

urlpatterns = patterns('killerkyle.views',
    
    #Main page
    url(r'^$', homePage.as_view(), name='home'),
    
    #Access to admin console
    url(r'^admin/', include(admin.site.urls)),
    
) 