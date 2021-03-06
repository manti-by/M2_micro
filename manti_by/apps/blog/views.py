import logging

from django.http import Http404
from django.shortcuts import render
from django.core.cache import cache
from django.utils.translation import gettext_lazy as _

from taggit.models import Tag

from manti_by.apps.core.utils import update_cache
from manti_by.apps.blog.models import Post

logger = logging.getLogger(__name__)


def index(request):
    tag = request.GET.get("tag")
    cache_key = "blog-%s-%s-%s" % (request.LANGUAGE_CODE, request.user.id, tag)
    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data

    if tag:
        try:
            tag = Tag.objects.get(slug__iexact=tag)
            item_list = Post.objects.filter(tags__slug=tag.slug).order_by("-created")[
                :6
            ]
        except Tag.DoesNotExist as e:
            logger.exception(e)
            item_list = []
    else:
        item_list = Post.objects.order_by("-created")[:6]

    cached_data = render(
        request, "blog/list.html", {"item_list": item_list, "tag": tag}
    )
    return update_cache(cache_key, cached_data)


def post(request, slug):
    cache_key = "post-%s-%s-%s" % (slug, request.LANGUAGE_CODE, request.user.id)
    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data
    try:
        item = Post.objects.get(slug__iexact=slug)
        template = "blog/post.html" if item.is_music else "blog/simple.html"

        cached_data = render(request, template, {"item": item})
        return update_cache(cache_key, cached_data)
    except Post.DoesNotExist as e:
        logger.exception(e)
        raise Http404(_("Post with slug %s does not exists") % slug)
