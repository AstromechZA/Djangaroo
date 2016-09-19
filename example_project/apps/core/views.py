from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.shortcuts import render
from django.views import View


def error_view(request, error):
    if error == 404:
        return render(request, '404.html', {'request_path': request.path, 'exception': unicode(Http404("Path not found"))}, status=404)
    elif error == 500:
        return render(request, '500.html', status=500)
    elif error == 403:
        return render(request, '403.html', {'exception': unicode(PermissionDenied("You were denied permission"))}, status=403)
    elif error == 400:
        return render(request, '400.html', status=400)
    raise ValueError("Error view does not handle %s" % error)
