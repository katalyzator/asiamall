# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from fcm_django.models import FCMDevice

from entertainments.models import EntertainmentLike, Entertainment
from foodcourt.models import FoodCourtLike, FoodCourt
from services.models import ServiceLike, Service
from .models import *

logger = logging.getLogger(__name__)


@csrf_exempt
def like_button_view(request):
    if request.method == 'POST':
        try:
            try:
                device_id = request.POST.get('device_id')
                value = request.POST.get('value')
                shop_id = request.POST.get('id')
                type_of_shop = request.POST.get('type_of_shop')
            except Exception as exc:
                logger.error(exc)
                return JsonResponse({
                    "result": u"{}".format(str(exc))
                })

            if type_of_shop == 'shop':
                if ShopLike.objects.filter(shop_id=shop_id, device__device_id=str(device_id)).exists():

                    shop = Shop.objects.get(id=shop_id)
                    shop_like = ShopLike.objects.get(shop_id=shop_id, device__device_id=str(device_id))
                    value = int(value)
                    shop_like.value = value
                    shop_like.save()
                    like_count = shop.like_counts
                    shop.like_counts = like_count + value
                    shop.save()

                    return JsonResponse({
                        "result": True
                    })

                else:
                    value = int(value)
                    shop = Shop.objects.get(id=shop_id)
                    ShopLike.objects.create(shop=shop,
                                            device=FCMDevice.objects.get(device_id=device_id), value=value)
                    like_count = shop.like_counts

                    shop.like_counts = like_count + int(value)
                    shop.save()

                    return JsonResponse({
                        "result": True
                    })

            elif type_of_shop == 'entertainment':
                if EntertainmentLike.objects.filter(shop_id=shop_id, device__device_id=device_id).exists():

                    shop = Entertainment.objects.get(id=shop_id)
                    shop_like = EntertainmentLike.objects.get(shop_id=shop_id, device__device_id=device_id)
                    shop_like.value = int(value)
                    like_count = shop.like_counts
                    shop.like_counts = like_count + int(value)
                    shop_like.save()
                    shop.save()

                    return JsonResponse({
                        "result": True
                    })

                else:
                    value = int(value)
                    shop = Entertainment.objects.get(id=shop_id)
                    EntertainmentLike.objects.create(shop=shop,
                                                     device=FCMDevice.objects.get(device_id=device_id),
                                                     value=int(value))
                    like_count = shop.like_counts
                    shop.like_counts = like_count + int(value)

                    shop.save()

                    return JsonResponse({
                        "result": True
                    })

            elif type_of_shop == 'service':
                if ServiceLike.objects.filter(shop_id=shop_id, device__device_id=device_id).exists():

                    shop = Service.objects.get(id=shop_id)
                    shop_like = ServiceLike.objects.get(shop_id=shop_id, device__device_id=device_id)
                    shop_like.value = int(value)
                    like_count = shop.like_counts
                    shop.like_counts = like_count + int(value)
                    shop_like.save()
                    shop.save()

                    return JsonResponse({
                        "result": True
                    })

                else:

                    shop = Service.objects.get(id=shop_id)
                    ServiceLike.objects.create(shop=shop,
                                               device=FCMDevice.objects.get(device_id=device_id), value=int(value))
                    like_count = shop.like_counts
                    shop.like_counts = like_count + int(value)
                    shop.save()

                    return JsonResponse({
                        "result": True
                    })

            elif type_of_shop == 'foodcourt':
                if FoodCourtLike.objects.filter(shop_id=shop_id, device__device_id=device_id).exists():

                    shop = FoodCourt.objects.get(id=shop_id)
                    shop_like = FoodCourtLike.objects.get(shop_id=shop_id, device__device_id=device_id)
                    shop_like.value = int(value)
                    like_count = shop.like_counts
                    shop.like_counts = like_count + int(value)
                    shop_like.save()
                    shop.save()

                    return JsonResponse({
                        "result": True
                    })

                else:

                    shop = FoodCourt.objects.get(id=shop_id)
                    FoodCourtLike.objects.create(shop=shop,
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


@csrf_exempt
def get_liked_shop(request):
    try:
        device_id = request.GET.get('device_id')

        try:

            if ShopLike.objects.filter(device__device_id=device_id).exists():
                shops = Shop.objects.filter(shop_likes__device__device_id=device_id)

            else:
                shops = None

            if ServiceLike.objects.filter(device__device_id=device_id).exists():
                services = Service.objects.filter(shop_likes__device__device_id=device_id)

            else:
                services = None

            if FoodCourtLike.objects.filter(device__device_id=device_id).exists():
                food_courts = FoodCourt.objects.filter(shop_likes__device__device_id=device_id)

            else:
                food_courts = None

            if EntertainmentLike.objects.filter(device__device_id=device_id).exists():
                entertainments = Entertainment.objects.filter(shop_likes__device__device_id=device_id)

            else:
                entertainments = None

            return JsonResponse({
                "result": {
                    "shops": [{
                        "id": u"{}".format(shop.id).encode("utf-8"),
                        "type_of_shop": "shop",
                        "title": u"{}".format(shop.title).encode("utf-8"),
                        "image": u"{}{}{}".format("http://", request.get_host(), shop.image.url).encode("utf-8"),
                        "logo": (u"{}{}{}".format("http://", request.get_host(), shop.logo.url).encode(
                            "utf-8")) if shop.logo else None,
                    } for shop in shops if shops is not None],

                    "services": [{
                        "id": u"{}".format(shop.id).encode("utf-8"),
                        "type_of_shop": "service",
                        "title": u"{}".format(shop.title).encode("utf-8"),
                        "image": u"{}{}{}".format("http://", request.get_host(), shop.image.url).encode("utf-8"),
                        "logo": (u"{}{}{}".format("http://", request.get_host(), shop.logo.url).encode(
                            "utf-8")) if shop.logo else None,
                    } for shop in services if services is not None],

                    "food_courts": [{
                        "id": u"{}".format(shop.id).encode("utf-8"),
                        "type_of_shop": "foodcourt",
                        "title": u"{}".format(shop.title).encode("utf-8"),
                        "image": u"{}{}{}".format("http://", request.get_host(), shop.image.url).encode("utf-8"),
                        "logo": (u"{}{}{}".format("http://", request.get_host(), shop.logo.url).encode(
                            "utf-8")) if shop.logo else None,
                    } for shop in food_courts if food_courts is not None],

                    "entertainments": [{
                        "id": u"{}".format(shop.id).encode("utf-8"),
                        "type_of_shop": "entertainment",
                        "title": u"{}".format(shop.title).encode("utf-8"),
                        "image": u"{}{}{}".format("http://", request.get_host(), shop.image.url).encode("utf-8"),
                        "logo": (u"{}{}{}".format("http://", request.get_host(), shop.logo.url).encode(
                            "utf-8")) if shop.logo else None,
                    } for shop in entertainments if entertainments is not None],

                }
            })

        except:
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


def detail_shop_view(request):
    try:
        device_id = request.GET.get('device_id')
        shop_id = request.GET.get('shop_id')

        shop = Shop.objects.get(id=shop_id)

        if ShopLike.objects.filter(device__device_id=device_id, shop_id=shop_id).exists():
            like_value = ShopLike.objects.get(device__device_id=device_id, shop_id=shop_id)
            if like_value.value == 1:
                is_liked = True
            else:
                is_liked = False
        else:
            is_liked = False

        return JsonResponse({
            "result": {
                "id": shop.id,
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
