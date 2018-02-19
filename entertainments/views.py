# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
from django.http import JsonResponse

from entertainments.models import Entertainment, EntertainmentLike

logger = logging.getLogger(__name__)


def detail_entertainment_view(request):
    try:
        device_id = request.GET.get('device_id')
        shop_id = request.GET.get('shop_id')

        shop = Entertainment.objects.get(id=shop_id)

        if EntertainmentLike.objects.filter(device__device_id=device_id, shop_id=shop_id).exists():
            is_liked = True
        else:
            is_liked = False

        return JsonResponse({
            "result": {
                "id": u"{}".format(shop.id).encode("utf-8"),
                "title": u"{}".format(shop.title).encode("utf-8"),
                "description": u"{}".format(shop.description).encode("utf-8"),
                "full_description": u"{}".format(shop.full_description).encode("utf-8"),
                "time_start": u"{}".format(shop.time_start).encode("utf-8"),
                "time_end": u"{}".format(shop.time_end).encode("utf-8"),
                "instagram": shop.instagram,
                "is_liked": is_liked,
                "facebook": shop.facebook,
                "like_counts": shop.like_counts,
                "phone_number": shop.phone_number,
                "share_url": shop.share_url,
                "image": u"{}{}{}".format("http://", request.get_host(), shop.image.url).encode("utf-8"),
                "logo": (u"{}{}{}".format("http://", request.get_host(), shop.logo.url).encode(
                    "utf-8")) if shop.logo else None,
                "timestamp": u"{}".format(shop.timestamp.strftime('%Y-%m-%d')).encode("utf-8")
            }
        })

    except Exception as exc:

        logger.error(exc)

        return JsonResponse({
            "result": u"{}".format(str(exc))
        })
