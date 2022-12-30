from ..models.album_page import AlbumPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(AlbumPage)
class AlbumPageAdmin(BasePageAdmin):
    pass
