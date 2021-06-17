import enum

from typing_extensions import Required

from django.contrib.postgres.fields.jsonb import JSONField
from care.facility.models.facility import Facility
from django.db import models

from care.users.models import User
from care.utils.models.base import BaseModel


class Location(BaseModel):
    name = models.CharField(max_length=1024, blank=False, null=False)
    description = models.TextField(default="", null=True, blank=True)
    facility = models.ForeignKey(Facility, on_delete=models.PROTECT, null=False, blank=False)


class Asset(BaseModel):
    class AssetType(enum.Enum):
        INTERNAL = 50
        EXTERNAL = 100

    AssetTypeChoices = [(e.value, e.name) for e in AssetType]

    class Status(enum.Enum):
        ACTIVE = 50
        TRANSFER_IN_PROGRESS = 100

    StatusChoices = [(e.value, e.name) for e in Status]

    name = models.CharField(max_length=1024, blank=False, null=False)
    description = models.TextField(default="", null=True, blank=True)
    asset_type = models.IntegerField(choices=AssetTypeChoices, default=AssetType.INTERNAL.value)
    status = models.IntegerField(choices=StatusChoices, default=Status.ACTIVE.value)
    current_location = models.ForeignKey(Location, on_delete=models.PROTECT, null=False, blank=False)
    is_working = models.BooleanField(default=None)
    serial_number = models.CharField(max_length=1024, blank=True, null=True)
    warranty_details = models.TextField(null=True, blank=True, default="")
    meta = JSONField(default=dict)


class UserDefaultLocation(BaseModel):
    user = models.ForeignKey("User", on_delete=models.PROTECT, null=False, blank=False)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, null=False, blank=False)


class FacilityDefaultLocation(BaseModel):
    facility = models.ForeignKey(Facility, on_delete=models.PROTECT, null=False, blank=False)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, null=False, blank=False)


class AssetTransaction(BaseModel):
    from_location = models.ForeignKey(Location, on_delete=models.PROTECT, null=False, blank=False)
    to_location = models.ForeignKey(Location, on_delete=models.PROTECT, null=False, blank=False)
    performed_by = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)