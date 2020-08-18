from django.views.generic import DetailView
from competitie_manager_app.models.competition import Competition
from competitie_manager_app.models.team import Team
from competitie_manager_app.models.team_competition import TeamCompetition


class CompetitionDetailView(DetailView):
    model = Competition
    context_object_name = 'competition_detail'
    template_name = 'competition_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CompetitionDetailView, self).get_context_data(**kwargs)
        competition = self.get_object()
        query_set_team = Team.objects.filter(
            competition=competition).order_by('naam')

        query_set = TeamCompetition.objects.filter(
            competition=competition).order_by('points').order_by('-points')

        context.update({'teams_detail': query_set_team,
                        'competition_teams_detail': query_set})

        return context
