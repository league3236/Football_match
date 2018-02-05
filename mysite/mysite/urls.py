from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^Eyedtt/', include('Eyedtt.urls')),
    url(r'^elections', include('elections.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
