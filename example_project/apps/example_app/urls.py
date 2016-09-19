from django.conf.urls import url

from example_project.apps.example_app.views import examples as example_views

app_name = 'examples'

urlpatterns = [
    url(r'^$', example_views.ExamplesView.as_view(), name='list_examples'),
    url(r'^new/?', example_views.NewExampleView.as_view(), name='new_example'),
    url(r'^(?P<example_id>\d+)/delete/?', example_views.DeleteExampleView.as_view(), name='delete_example'),
    url(r'^(?P<example_id>\d+)/edit/?', example_views.EditExampleView.as_view(), name='edit_example'),
    url(r'^(?P<example_id>\d+)/?', example_views.ExamplesInstanceView.as_view(), name='view_example'),
]
