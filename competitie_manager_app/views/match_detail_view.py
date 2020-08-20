from django.views.generic import DetailView
from competitie_manager_app.models.competition import Competition
from competitie_manager_app.models.team import Team
from competitie_manager_app.models.team_competition import TeamCompetition
from competitie_manager_app.models.match import Match

# Class to render detail page of a match
class MatchDetailView(DetailView):
    model = Match
    context_object_name = 'match_detail'
    template_name = 'match_detail.html'
