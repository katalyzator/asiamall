# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from main.models import Slider
from news.models import News
from promotions.models import Promotion
from shops.models import Shop, Category

logger = logging.getLogger(__name__)


@csrf_exempt
def get_main_page_values(request):
    try:
        news = News.objects.all()[:3]
        promotions = Promotion.objects.all()[:3]
        slider = Slider.objects.all()[:5]

        return JsonResponse({
            "result": {
                "news": [{
                    "title": u"{}".format(new.title).encode("utf-8"),
                    "image": (u"{}{}{}".format("http://", request.get_host(), new.image.url)).encode(
                        "utf-8") if new.image else None,
                    "video": (u"{}{}{}".format("http://", request.get_host(), new.video.url)).encode(
                        "utf-8") if new.video else None,
                    "tag": u"{}".format(new.tag).encode("utf-8"),
                    "text": u"{}".format(new.text).encode("utf-8"),
                    "timestamp": u"{}".format(new.timestamp.strftime('%Y-%m-%d')).encode("utf-8")

                } for new in news],

                "promotions": [{
                    "title": u"{}".format(promotion.title).encode("utf-8"),
                    "image": u"{}{}{}".format("http://", request.get_host(), promotion.image.url).encode("utf-8"),
                    "tag": u"{}".format(promotion.tag).encode("utf-8"),
                    "phone_number": u"{}".format(promotion.phone_number).encode("utf-8"),
                    "text": u"{}".format(promotion.text).encode("utf-8"),
                    "timestamp": u"{}".format(promotion.timestamp.strftime('%Y-%m-%d')).encode("utf-8")

                } for promotion in promotions],

                "slider": [{
                    "title": u"{}".format(slide.title).encode("utf-8"),
                    "image": u"{}{}{}".format("http://", request.get_host(), slide.image.url).encode("utf-8")
                } for slide in slider]

            }
        })

    except Exception as exc:

        logger.error(exc)

        return JsonResponse({
            "result": u"{}".format(str(exc))
        })


def search_view(request):
    try:
        q = request.GET.get('value')

        if q:
            shops = Shop.objects.filter(full_description__icontains=q)
            news = News.objects.filter(title__icontains=q)
            promotions = Promotion.objects.filter(title__icontains=q)

            return JsonResponse({
                "result": {
                    "news": [{
                        "title": u"{}".format(new.title).encode("utf-8"),
                        "image": (u"{}{}{}".format("http://", request.get_host(), new.image.url)).encode(
                            "utf-8") if new.image else None,
                        "video": (u"{}{}{}".format("http://", request.get_host(), new.video.url)).encode(
                            "utf-8") if new.video else None,
                        "tag": u"{}".format(new.tag).encode("utf-8"),
                        "text": u"{}".format(new.text).encode("utf-8"),
                        "timestamp": u"{}".format(new.timestamp.strftime('%Y-%m-%d')).encode("utf-8")

                    } for new in news],

                    "promotions": [{
                        "title": u"{}".format(promotion.title).encode("utf-8"),
                        "image": u"{}{}{}".format("http://", request.get_host(), promotion.image.url).encode("utf-8"),
                        "tag": u"{}".format(promotion.tag).encode("utf-8"),
                        "phone_number": u"{}".format(promotion.phone_number).encode("utf-8"),
                        "text": u"{}".format(promotion.text).encode("utf-8"),
                        "timestamp": u"{}".format(promotion.timestamp.strftime('%Y-%m-%d')).encode("utf-8")

                    } for promotion in promotions],

                    "shops": [{
                        "title": u"{}".format(shop.title).encode("utf-8"),
                        "description": u"{}".format(shop.description).encode("utf-8"),
                        "full_description": u"{}".format(shop.full_description).encode("utf-8"),
                        "time_start": u"{}".format(shop.time_start).encode("utf-8"),
                        "time_end": u"{}".format(shop.time_end).encode("utf-8"),
                        "image": u"{}{}{}".format("http://", request.get_host(), shop.image.url).encode("utf-8"),
                        "logo": (u"{}{}{}".format("http://", request.get_host(), shop.logo.url).encode("utf-8")) if shop.logo else None,
                        "timestamp": u"{}".format(shop.timestamp.strftime('%Y-%m-%d')).encode("utf-8")
                    } for shop in shops]

                }
            })

    except Exception as exc:

        logger.error(exc)

        return JsonResponse({
            "result": u"{}".format(str(exc))
        })
