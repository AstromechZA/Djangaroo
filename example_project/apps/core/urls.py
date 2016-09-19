from django.conf.urls import url
from django.views.generic.base import RedirectView
from example_project.apps.core.views import error_view

app_name = 'core'

urlpatterns = [
    url(r'^404/?', error_view, {'error': 404}),
    url(r'^500/?', error_view, {'error': 500}),
    url(r'^403/?', error_view, {'error': 403}),
    url(r'^400/?', error_view, {'error': 400}),
    url(r'^$', RedirectView.as_view(url='examples', permanent=False), name='index'),
]
