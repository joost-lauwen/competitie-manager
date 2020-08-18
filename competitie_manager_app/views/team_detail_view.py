from django.views.generic import DetailView
from competitie_manager_app.models.team import Team

class TeamDetailView(DetailView):
    model = Team
    context_object_name = 'team_detail'
    template_name = 'team_detail.html'
