import uuid

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
    company = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name=_("entreprise"), null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()  # Default manager is always the first one to be declared.

    class Meta:
        verbose_name = _("utilisateur")
        verbose_name_plural = _("utilisateurs")

    def __str__(self):
        return self.email
    
    
class AbstractToken(models.Model):

    class Meta:
        abstract = True
        
    key = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name=_("clé"))
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name=_("utilisateur"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date d'ajout"))
    is_used = models.BooleanField(default=False, verbose_name=_("est utilisé"))


class ResetPasswordToken(AbstractToken):
    pass