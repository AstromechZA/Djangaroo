from django.contrib import admin

from example_project.apps.example_app.models import Example


@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):

    def get_ordering(self, request):
        return ['name']
