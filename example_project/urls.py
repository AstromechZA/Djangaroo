from django.conf.urls import url, include
from django.contrib import admin

from example_project.apps.core import urls as core_urls
from example_project.apps.example_app import urls as example_urls
from example_project.apps.example_api import urls as api_urls


urlpatterns = [
    url(r'^api/examples/', include(api_urls)),
    url(r'^examples/', include(example_urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(core_urls)),
]
