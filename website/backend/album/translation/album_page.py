from modeltranslation.translator import TranslationOptions, register
from ..models import AlbumPage


@register(AlbumPage)
class AlbumPageTranslationOptions(TranslationOptions):
    pass
