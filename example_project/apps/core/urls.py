from django.conf.urls import url
from django.views.generic.base import RedirectView

from example_project.apps.core import views

app_name = 'core'

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='example', permanent=False), name='index'),
]
