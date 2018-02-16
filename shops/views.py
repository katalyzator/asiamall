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
                ShopLike.objects.get(shop_id=shop_id, device_id=device_id)
                like_count = shop.like_counts
                shop.like_counts = like_count + int(value)
                shop.save()

                return JsonResponse({
                    "result": True
                })

            else:

                shop = Shop.objects.get(id=shop_id)
                ShopLike.objects.create(shop=shop,
                                        device=FCMDevice.objects.get(device_id=device_id))
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
