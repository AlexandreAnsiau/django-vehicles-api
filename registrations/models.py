from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
from commons.models import AbstractDatedModel, AbstractUUIDModel
from companies.models import Company


class CustomUser(AbstractUUIDModel, AbstractDatedModel, AbstractUser):
    username = None
    email = models.EmailField(max_length=500, unique=True)
    is_active = models.BooleanField(blank=True, default=True)
    is_staff = models.BooleanField(blank=True, default=False)
    is_superuser = models.BooleanField(blank=True, default=False)
    is_visible = models.BooleanField(blank=True, default=True)
    first_name = models.CharField(max_length=100, verbose_name=_("prénom"))
    last_name = models.CharField(max_length=100, verbose_name=_("nom de famille"))
    company = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name=_("entreprise"))
    slug = models.SlugField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()  # Default manager is always the first one to be declared.

    class Meta:
        verbose_name = _("utilisateur")
        verbose_name_plural = _("utilisateurs")

    def save(self, **kwargs):
        self.slug = slugify(f"{self.first_name}-{self.last_name}")
        super().save(**kwargs)

    def __str__(self):
        return f"{self.first_name.title()} {self.last_name.title()}"