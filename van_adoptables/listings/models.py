from django.db import models
from organizations.models import Organization


class Listing(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
