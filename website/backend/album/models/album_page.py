from garpix_page.models import BasePage


class AlbumPage(BasePage):
    template = "pages/album.html"

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"
        ordering = ("-created_at",)
