from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .sport import Sport

class Competition(models.Model):
    naam = models.CharField(max_length=50, unique=True)
    sport_soort = models.ForeignKey(Sport, null=True, on_delete=models.SET_NULL, related_name='sport_competitie')
    made_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='competition_owner', blank=True)


    def __str__(self):
        return self.naam

    def get_absolute_url(self):
        return reverse('competitie_manager_app:competition_detail', kwargs={"pk": self.pk})
