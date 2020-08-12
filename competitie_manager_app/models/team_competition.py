from django.db import models
from .team import Team
from .competition import Competition

class TeamCompetition(models.Model):
    team = models.ForeignKey(Team, models.DO_NOTHING)
    competition = models.ForeignKey(Competition, models.DO_NOTHING)
    points = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.competition.naam + ' // ' + self.team.naam
