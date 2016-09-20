from django.conf.urls import url

from example_project.apps.example_api.views import examples as example_api_views

app_name = 'examples_api'


urlpatterns = [
    url(r'^(?P<example_id>\d+)/?$', example_api_views.view_example, name='view_example'),
    url(r'^$', example_api_views.list_examples, name='list_examples'),
]
