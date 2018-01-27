from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('main.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
]
