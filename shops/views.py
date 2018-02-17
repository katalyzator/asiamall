# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.http import JsonResponse
from django.shortcuts import render
from fcm_django.models import FCMDevice

from shops.models import ShopLike, Shop

logger = logging.getLogger(__name__)


def like_button_view(request):
    if request.method == 'POST':
        try:
            try:
                device_id = request.POST.get('device_id')
                value = request.POST.get('value', int)
                shop_id = request.POST.get('shop_id')
            except Exception as exc:
                logger.error(exc)
                return JsonResponse({
                    "result": u"{}".format(str(exc))
                })

            if ShopLike.objects.filter(shop_id=shop_id, device_id=device_id).exists():

                shop = Shop.objects.get(id=shop_id)
                shop_like = ShopLike.objects.get(shop_id=shop_id, device_id=device_id)
                shop_like.value = int(value)
                like_count = shop.like_counts
                shop.like_counts = like_count + int(value)
                shop.save()

                return JsonResponse({
                    "result": True
                })

            else:

                shop = Shop.objects.get(id=shop_id)
                ShopLike.objects.create(shop=shop,
                                        device=FCMDevice.objects.get(device_id=device_id), value=int(value))
                like_count = shop.like_counts
                shop.like_counts = like_count + int(value)
                shop.save()

                return JsonResponse({
                    "result": True
                })

        except Exception as exc:
            logger.error(exc)
            return JsonResponse({
                "result": u"{}".format(str(exc))
            })

    return JsonResponse({
        "result": "Request method is 'GET', you must send 'POST' request"
    })


def get_liked_shop(request):
    try:
        device_id = request.GET.get('device_id')

        if ShopLike.objects.filter(device__device_id=device_id).exists():
            shops = Shop.objects.filter(shop_likes__device__device_id=device_id)

            return JsonResponse({
                "result": {
                    "shops": [{
                        "title": u"{}".format(shop.title).encode("utf-8"),
                        "description": u"{}".format(shop.description).encode("utf-8"),
                        "full_description": u"{}".format(shop.full_description).encode("utf-8"),
                        "time_start": u"{}".format(shop.time_start).encode("utf-8"),
                        "time_end": u"{}".format(shop.time_end).encode("utf-8"),
                        "instagram": u"{}".format(shop.instagram).encode("utf-8"),
                        "facebook": u"{}".format(shop.facebook).encode("utf-8"),
                        "image": u"{}{}{}".format("http://", request.get_host(), shop.image.url).encode("utf-8"),
                        "logo": (u"{}{}{}".format("http://", request.get_host(), shop.logo.url).encode(
                            "utf-8")) if shop.logo else None,
                        "timestamp": u"{}".format(shop.timestamp.strftime('%Y-%m-%d')).encode("utf-8")
                    } for shop in shops]
                }
            })

        else:
            return JsonResponse({
                "result": {
                    None
                }
            })

    except Exception as exc:

        logger.error(exc)

        return JsonResponse({
            "result": u"{}".format(str(exc))
        })
