from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from example_project.apps.example_app.forms.new_example_form import NewExampleForm
from example_project.apps.example_app.models import Example


class ExamplesView(View):

    def get(self, request):
        return render(request, 'examples/list_examples.html', {
            'examples': Example.objects.all()
        })


class NewExampleView(View):

    def get(self, request):
        form = NewExampleForm()
        return render(request, 'examples/new_example.html', {'egform': form})

    def post(self, request):
        form = NewExampleForm(request.POST)
        if form.is_valid():
            return redirect(form.save())

        return render(request, 'examples/new_example.html', {'egform': form}, status=400)


class DeleteExampleView(View):

    def post(self, request, example_id):
        get_object_or_404(Example, pk=example_id).delete()
        return redirect('examples:list_examples')


class EditExampleView(View):

    def get(self, request, example_id):
        eg = get_object_or_404(Example, pk=example_id)
        form = NewExampleForm(instance=eg)
        return render(request, 'examples/edit_example.html', {'eg': eg, 'egform': form})

    def post(self, request, example_id):
        eg = get_object_or_404(Example, pk=example_id)
        form = NewExampleForm(request.POST)
        if form.is_valid():
            return redirect(form.save())

        return render(request, 'examples/edit_example.html', {'eg': eg, 'egform': form}, status=400)

class ExamplesInstanceView(View):

    def get(self, request, example_id):
        eg = get_object_or_404(Example, pk=example_id)
        return render(request, 'examples/view_example.html', {'example': eg})
