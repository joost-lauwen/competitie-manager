from django.views.generic import ListView
from competitie_manager_app.models.team import Team

# Class to render the list view of the team model
class TeamListView(ListView):
    model = Team
    context_object_name = 'team_list'
    template_name = 'team_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Team.objects.all().order_by('naam')
