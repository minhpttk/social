import datetime

from django.db import models

from core.managers import SoftDeleteManager


class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(null=True)
    objects = SoftDeleteManager()
    all_objects = models.Manager()

    def soft_delete(self):
        self.deleted_at = datetime.datetime.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True


class TimestampsModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UnsignedIntegerField(models.Field):
    def db_type(self, connection):
        return 'integer UNSIGNED'
