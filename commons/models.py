from pathlib import Path
import uuid

from django.conf import settings
from django.db import models
from django.db.models.fields.files import FileField
from django.utils.translation import gettext_lazy as _


class AbstractDatedModel(models.Model):

    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("créé à"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("modifié à"))


class AbstractUUIDModel(models.Model):

    class Meta:
        abstract = True

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 


class AbstractFileModel(models.Model):

    class Meta:
        abstract = True

    def delete(self):
        for field in self._meta.fields:
            if isinstance(field, FileField):
                file = getattr(self, field.name)
                if file:
                    file_path = Path(file.path)
                    if file_path.is_file() and settings.MEDIA_DEFAULT not in file_path.parents:
                        file_path.unlink()
        super().delete()