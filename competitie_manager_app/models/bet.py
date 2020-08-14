from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .match import Match
from .team_competition import TeamCompetition


class Bet(models.Model):
    user = models.ForeignKey(
        User, null=False, on_delete=models.CASCADE, related_name='gambler', blank=False)
    stake = models.IntegerField(null=True, default=1)
    gamble = models.IntegerField(null=True, default=1)
    match = models.ForeignKey(
        Match, null=False, on_delete=models.CASCADE, related_name='bet_match', blank=False)
    bet_result = models.BooleanField(default=False)
    quotation_h_team = models.DecimalField(decimal_places=2, max_digits=9999)
    quotation_a_team = models.DecimalField(decimal_places=2, max_digits=9999)
    quotation_draw = models.DecimalField(decimal_places=2, max_digits=9999)

    def __str__(self):
        return self.user.username + ' // ' + self.match.home_team.naam + ' vs ' + self.match.away_team.naam

    def get_absolute_url(self):
        return reverse('competitie_manager_app:bet_detail', kwargs={"competitie": self.match.competition, "match_pk": self.match.pk, "pk": self.pk})

    def get_quotation_h_team(self):
        h_team_points = TeamCompetition.objects.get(
            competition=self.match.competition, team=self.match.home_team).points
        a_team_points = TeamCompetition.objects.get(
            competition=self.match.competition, team=self.match.away_team).points

        if h_team_points > a_team_points:
            return 1.25
        elif h_team_points < a_team_points:
            return 1.75
        else:
            return 1.5

    def get_quotation_a_team(self):
        h_team_points = TeamCompetition.objects.get(
            competition=self.match.competition, team=self.match.home_team).points
        a_team_points = TeamCompetition.objects.get(
            competition=self.match.competition, team=self.match.away_team).points

        if h_team_points > a_team_points:
            return 2
        elif h_team_points < a_team_points:
            return 1.5
        else:
            return 1.75

    def get_quotation_draw(self):
        h_team_points = TeamCompetition.objects.get(
            competition=self.match.competition, team=self.match.home_team).points
        a_team_points = TeamCompetition.objects.get(
            competition=self.match.competition, team=self.match.away_team).points

        if h_team_points > a_team_points:
            return 1.5
        elif h_team_points < a_team_points:
            return 1.75
        else:
            return 1.25
