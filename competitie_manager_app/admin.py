from django.contrib import admin
from competitie_manager_app.models.sport import Sport
from competitie_manager_app.models.competition import Competition
from competitie_manager_app.models.team import Team
from competitie_manager_app.models.team_competition import TeamCompetition
from competitie_manager_app.models.match import Match
from competitie_manager_app.models.bet import Bet
from competitie_manager_app.models.user_toto_info import UserTotoInfo

# Register your models here.
admin.site.register(Sport)
admin.site.register(Competition)
admin.site.register(Team)
admin.site.register(TeamCompetition)
admin.site.register(Match)
admin.site.register(Bet)
admin.site.register(UserTotoInfo)
