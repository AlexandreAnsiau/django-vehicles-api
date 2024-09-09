from django.db import models
from django.utils.translation import gettext_lazy as _

from commons.models import AbstractDatedModel, AbstractUUIDModel


class Company(AbstractUUIDModel, AbstractDatedModel):
    name = models.CharField(max_length=200, verbose_name=_("nom"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Entreprise")
        verbose_name_plural = _("Entreprises")