from django.db import models

class Competition(models.Model):
    naam = models.CharField(max_length=50)

    def __str__(self):
        return self.naam
