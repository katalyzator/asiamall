
from modeltranslation.translator import TranslationOptions, translator

from shops.models import Shop


class ShopTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'full_description')


translator.register(Shop, ShopTranslationOptions)
