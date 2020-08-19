from django.db import models

# Model for the Sport class. This model contains info about the sports.
class Sport(models.Model):
    naam = models.CharField(max_length=50)

    def __str__(self):
        return self.naam
