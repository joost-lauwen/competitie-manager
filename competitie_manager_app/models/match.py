from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .competition import Competition


class Match(models.Model):
    home_team = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name='match_home_team')
    away_team = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name='match_away_team')
    competition = models.ForeignKey(
        Competition, null=True, on_delete=models.SET_NULL, related_name='competition_match')
    result = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.competition.naam + ' // ' + self.home_team + ' vs ' + self.away_team
