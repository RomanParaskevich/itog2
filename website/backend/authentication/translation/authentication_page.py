from modeltranslation.translator import TranslationOptions, register
from ..models import AuthenticationPage


@register(AuthenticationPage)
class AuthenticationPageTranslationOptions(TranslationOptions):
    pass
