from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
# import blog.views
# from views import getPageContent

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^(.*)$', 'gettingstarted.views.getPageContent', name='getPageContent'),
)
