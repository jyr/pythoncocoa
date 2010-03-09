from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   (r'^admin/', include(admin.site.urls)),
   (r'^', include('cms.urls'))
)

urlpatterns += patterns('django.views', (r'^media/(?P<path>.*)$', 'static.serve', {'document_root': settings.STATIC_DOC_ROOT}))