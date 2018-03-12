from modeltranslation.translator import TranslationOptions, translator, register

from main.models import AboutAsiaMall


class AboutAsiaMallTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


translator.register(AboutAsiaMall, AboutAsiaMallTranslationOptions)
