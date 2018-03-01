
from modeltranslation.translator import TranslationOptions, translator

from services.models import Service


class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'full_description')


translator.register(Service, ServiceTranslationOptions)
