from django.db import models
from django.contrib.auth.models import User
from .sport import Sport
from .competition import Competition
from django.urls import reverse

# Model for the Team class. This model contains info about the teams.
class Team(models.Model):
    naam = models.CharField(max_length=50, unique=True)
    made_by = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name='team_owner', blank=True)
    created_on = models.DateTimeField(auto_now=True)
    sport_soort = models.ForeignKey(
        Sport, null=False, on_delete=models.CASCADE, related_name='sport_team')
    competition = models.ManyToManyField(
        Competition, through='TeamCompetition')
    image = models.ImageField(
        upload_to='logos/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.naam

    def get_absolute_url(self):
        return reverse('competitie_manager_app:team_detail', kwargs={"pk": self.pk})
