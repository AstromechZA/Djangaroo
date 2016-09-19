from django.conf.urls import url, include
from django.contrib import admin
from django.views import defaults

from example_project.apps.core import urls as core_urls
from example_project.apps.example_app import urls as example_urls

urlpatterns = [
    url(r'^examples/', include(example_urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(core_urls)),
]
