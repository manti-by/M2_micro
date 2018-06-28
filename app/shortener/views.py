import logging

from django.http import Http404
from django.shortcuts import redirect

from shortener.models import Link


logger = logging.getLogger('app')


def shortener(request, short_link):
    try:
        link = Link.objects.get(short_link=short_link)
        return redirect(link.original_link, permanent=True)
    except Link.DoesNotExist:
        raise Http404