from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Item(models.Model):
    name = Model.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)