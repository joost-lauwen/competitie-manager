from django.db import models
from django.urls import reverse
from .competition import Competition
from .team_competition import TeamCompetition
from .team import Team

# Model for the Match class. This model contains info about the matches.
class Match(models.Model):
    home_team = models.ForeignKey(
        Team, null=True, on_delete=models.SET_NULL, related_name='match_home_team')
    away_team = models.ForeignKey(
        Team, null=True, on_delete=models.SET_NULL, related_name='match_away_team')
    competition = models.ForeignKey(
        Competition, null=True, on_delete=models.SET_NULL, related_name='competition_match')
    result = models.IntegerField(null=True, default=0)
    h_goals = models.IntegerField(null=True, default=0)
    a_goals = models.IntegerField(null=True, default=0)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.competition.naam + ' // ' + self.home_team.naam + ' vs ' + self.away_team.naam

    def get_absolute_url(self):
        return reverse('competitie_manager_app:match_detail', kwargs={"competitie": self.competition, "pk": self.pk})
