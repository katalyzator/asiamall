
from modeltranslation.translator import TranslationOptions, translator

from foodcourt.models import FoodCourt


class FoodCourtTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'full_description')


translator.register(FoodCourt, FoodCourtTranslationOptions)
