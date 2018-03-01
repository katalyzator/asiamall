from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from solid_i18n.urls import solid_i18n_patterns

from asiamall import settings

schema_view = get_swagger_view(title='Asiamall documentation')

urlpatterns = solid_i18n_patterns(
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/main/', include('main.urls')),
    url(r'^api/shop/', include('shops.urls')),
    url(r'^api/children/', include('childrens.urls')),
    url(r'^api/news/', include('news.urls')),
    url(r'^api/promotion/', include('promotions.urls')),
    url(r'^api/entertainment/', include('entertainments.urls')),
    url(r'^api/food_court/', include('foodcourt.urls')),
    url(r'^api/service/', include('services.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^documentation/$', schema_view),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
