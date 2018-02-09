from django.conf.urls import url, include

from main.views import get_main_page_values

urlpatterns = [
    url(r'^get_main_page_values/', get_main_page_values, name='get_main_page_values'),
]
