
from modeltranslation.translator import TranslationOptions, translator

from entertainments.models import Entertainment


class EntertainmentsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'full_description')


translator.register(Entertainment, EntertainmentsTranslationOptions)
