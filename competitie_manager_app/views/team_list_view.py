from django.views.generic import ListView
from competitie_manager_app.models.team import Team

class TeamListView(ListView):
    model = Team
    context_object_name = 'team_list'
    template_name = 'team_list.html'

    def get_queryset(self):
        return Team.objects.all().order_by('naam')
