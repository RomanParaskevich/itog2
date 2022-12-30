from garpix_page.models import BasePage


class AuthenticationPage(BasePage):
    template = "pages/authentication.html"

    class Meta:
        verbose_name = "Authentication"
        verbose_name_plural = "Authentications"
        ordering = ("-created_at",)
