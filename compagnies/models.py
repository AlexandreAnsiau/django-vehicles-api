from django.db import models
from django.utils.translation import gettext_lazy as _

from commons.models import AbstractDatedModel, AbstractUUIDModel


class Compagnies(AbstractUUIDModel, AbstractDatedModel):
    name = models.CharField(max_length=200, verbose_name=_("nom"))

    def __str__(self):
        return self.name