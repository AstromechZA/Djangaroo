from django.conf.urls import url

from example_project.apps.example_app.views import examples as example_views

app_name = 'examples'

urlpatterns = [
    url(r'^$', example_views.ListExamples.as_view(), name='list_examples'),
    url(r'^new/?', example_views.NewExample.as_view(), name='new_example'),
    url(r'^(?P<example_id>\d+)/delete/?', example_views.DeleteExample.as_view(), name='delete_example'),
    url(r'^(?P<example_id>\d+)/edit/?', example_views.EditExample.as_view(), name='edit_example'),
    url(r'^(?P<example_id>\d+)/?', example_views.ViewExample.as_view(), name='view_example'),
]
