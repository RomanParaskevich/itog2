from ..models.authentication_page import AuthenticationPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(AuthenticationPage)
class AuthenticationPageAdmin(BasePageAdmin):
    pass
