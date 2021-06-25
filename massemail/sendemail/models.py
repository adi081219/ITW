from django.db import models
import pandas as pd

# Create your models here.

class Newsletter(models.Model):
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.email

