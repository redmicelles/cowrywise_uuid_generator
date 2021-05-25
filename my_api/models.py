from django.db import models
from datetime import datetime

# Create your models here.

class Uuid(models.Model):
    uuid = models.UUIDField()
    time_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.uuid)