from django.db import models
from django.utils.translation import gettext_lazy as _

class Subscriber(models.Model):
    class Meta:
        verbose_name = _("Subscriber")
        verbose_name_plural = _("Subscribers")
        ordering = ['id']

    date = models.DateTimeField(auto_now_add=True, verbose_name=_("Subscribed Date"))
    email = models.EmailField(max_length=254)

    def __str__(self):
        return str(self.id)