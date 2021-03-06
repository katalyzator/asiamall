# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
from itertools import chain

from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from fcm_django.models import FCMDevice

from entertainments.models import Entertainment
from foodcourt.models import FoodCourt
from main.models import Slider, Application
from news.models import News
from promotions.models import Promotion
from services.models import Service
from shops.models import Shop

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
                    "title": u"{}".format(new.title).encode("utf-8") if new.title else None,
                    "image": (u"{}{}{}".format("http://", request.get_host(), new.image.url)).encode(
                        "utf-8") if new.image else None,
                    "video": (u"{}{}{}".format("http://", request.get_host(), new.video.url)).encode(
                        "utf-8") if new.video else None,
                    "tag": u"{}".format(new.tag.title).encode("utf-8"),
                    "share_url": new.share_url,
                    "text": u"{}".format(new.text).encode("utf-8"),
                    "timestamp": u"{}".format(new.timestamp.strftime('%Y-%m-%d')).encode("utf-8")

                } for new in news] if news else  None,

                "promotions": [{
                    "title": u"{}".format(promotion.title).encode("utf-8") if promotion.title else None,
                    "image": u"{}{}{}".format("http://", request.get_host(), promotion.image.url).encode("utf-8"),
                    "tag": u"{}".format(promotion.tag.title).encode("utf-8"),
                    "phone_number": u"{}".format(promotion.phone_number).encode("utf-8"),
                    "share_url": promotion.share_url,
                    "text": u"{}".format(promotion.text).encode("utf-8"),
                    "timestamp": u"{}".format(promotion.timestamp.strftime('%Y-%m-%d')).encode("utf-8")

                } for promotion in promotions] if promotions else  None,

                "slider": [{
                    "title": u"{}".format(slide.title).encode("utf-8") if slide.title else None,
                    "image": u"{}{}{}".format("http://", request.get_host(), slide.image.url).encode("utf-8")
                } for slide in slider] if slider else  None,

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
        shops = []

        if q:
            shops = Shop.objects.filter(full_description__icontains=q)
            news = News.objects.filter(title__icontains=q)
            promotions = Promotion.objects.filter(title__icontains=q)
            service = Service.objects.filter(title__icontains=q)
            foodcourt = FoodCourt.objects.filter(title__icontains=q)
            entertainments = Entertainment.objects.filter(title__icontains=q)
            shops_result = list(chain(shops, service, foodcourt, entertainments))

            return JsonResponse({
                "result": {
                    "news": [{
                        "title": u"{}".format(new.title).encode("utf-8"),
                        "image": (u"{}{}{}".format("http://", request.get_host(), new.image.url)).encode(
                            "utf-8") if new.image else None,
                        "video": (u"{}{}{}".format("http://", request.get_host(), new.video.url)).encode(
                            "utf-8") if new.video else None,
                        "tag": u"{}".format(new.tag.title).encode("utf-8"),
                        "share_url": u"{}".format(new.share_url).encode("utf-8"),
                        "text": u"{}".format(new.text).encode("utf-8"),
                        "timestamp": u"{}".format(new.timestamp.strftime('%Y-%m-%d')).encode("utf-8")

                    } for new in news],

                    "promotions": [{
                        "title": u"{}".format(promotion.title).encode("utf-8"),
                        "image": u"{}{}{}".format("http://", request.get_host(), promotion.image.url).encode("utf-8"),
                        "tag": u"{}".format(promotion.tag.title).encode("utf-8"),
                        "phone_number": u"{}".format(promotion.phone_number).encode("utf-8"),
                        "text": u"{}".format(promotion.text).encode("utf-8"),
                        "timestamp": u"{}".format(promotion.timestamp.strftime('%Y-%m-%d')).encode("utf-8")

                    } for promotion in promotions],

                    "shops": [{
                        "id": shop.id,
                        "title": u"{}".format(shop.title).encode("utf-8"),
                        "image": u"{}{}{}".format("http://", request.get_host(), shop.image.url).encode("utf-8"),
                        "logo": (u"{}{}{}".format("http://", request.get_host(), shop.logo.url).encode(
                            "utf-8")) if shop.logo else None,
                        "type_of_shop": "shop" if shop.__class__.__name__ == 'Shop' else "service" if shop.__class__.__name__ == 'Service' else "foodcourt" if shop.__class__.__name__ == 'FoodCourt' else "entertainment" if shop.__class__.__name__ == 'Entertainment' else 'shop',
                    } for shop in shops_result],

                }
            })

    except Exception as exc:

        logger.error(exc)

        return JsonResponse({
            "result": u"{}".format(str(exc))
        })


@csrf_exempt
def post_application(request):
    if request.method == 'POST':
        try:
            try:
                full_name = request.POST.get('full_name')
                phone = request.POST.get('phone')
                email = request.POST.get('email')
                square = request.POST.get('square')
                type_of_product = request.POST.get('type_of_product')
                brand = request.POST.get('brand')
            except Exception as exc:
                logger.error(exc)
                return JsonResponse({
                    "result": u"{}".format(str(exc))
                })

            Application.objects.create(
                full_name=full_name, phone=phone, email=email, square=square,
                type_of_product=type_of_product, brand=brand
            )

            return JsonResponse({
                "result": True
            })

        except Exception as exc:
            logger.error(exc)
            return JsonResponse({
                "result": u"{}".format(str(exc))
            })

    return JsonResponse({
        "result": "Request method is 'GET', please try again with 'POST' method"
    })


@csrf_exempt
def get_device_id(request):
    if request.method == 'POST':
        try:
            try:
                device_id = request.POST.get('device_id')
                device_token = request.POST.get('device_token')
                device_type = request.POST.get('device_type')
            except Exception as exc:
                logger.error(exc)
                return JsonResponse({
                    "result": u"{}".format(str(exc))
                })
            if device_type == 'ios':

                if FCMDevice.objects.filter(device_id=device_id).exists():
                    fcm = FCMDevice.objects.get(device_id=device_id)
                    fcm.registration_id = device_token
                    fcm.save()
                else:
                    FCMDevice.objects.create(registration_id=device_token, type=u'ios', device_id=device_id)

            elif device_type == 'android':
                if FCMDevice.objects.filter(device_id=device_id).exists():
                    fcm = FCMDevice.objects.get(device_id=device_id)
                    fcm.registration_id = device_token
                    fcm.save()
                else:
                    FCMDevice.objects.create(registration_id=device_token, type=u'android', device_id=device_id)

            else:
                FCMDevice.objects.create(registration_id=device_id, type=u'web')

            return JsonResponse({
                "result": True
            })

        except Exception as exc:
            logger.error(exc)
            return JsonResponse({
                "result": u"{}".format(str(exc))
            })

    return JsonResponse({
        "result": "Request method is 'GET', please try again with 'POST' method"
    })
