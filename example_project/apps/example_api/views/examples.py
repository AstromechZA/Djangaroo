from django.forms import model_to_dict
from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404

from example_project.apps.example_app.models import Example


def throw_errors_as_json(view_func):
    def __inner__(*args, **kwargs):
        try:
            return view_func(*args, **kwargs)
        except Http404 as e:
            return JsonResponse({'error': str(e)}, status=404)
        except Exception:
            return JsonResponse({'error': 'Internal error'}, status=500)
    return __inner__


@throw_errors_as_json
def list_examples(request):
    return JsonResponse({'list': [model_to_dict(e) for e in Example.objects.all()]})


@throw_errors_as_json
def view_example(request, example_id):
    e = get_object_or_404(Example, pk=example_id)
    return JsonResponse(model_to_dict(e))
