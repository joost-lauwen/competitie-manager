from django.views.generic import DetailView
from competitie_manager_app.models.competition import Competition
from competitie_manager_app.models.team import Team

# Class that handles the detailpage of a painting.
class CompetitionDetailView(DetailView):
    model = Competition
    context_object_name = 'competition_detail'
    template_name = 'competition_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CompetitionDetailView, self).get_context_data(**kwargs)
        competition = self.get_object()
        query_set = Team.objects.filter(competitie=competition).order_by('naam')
        context.update({'competition_teams_detail': query_set})

        return context
