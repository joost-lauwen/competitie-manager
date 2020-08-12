from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from competitie_manager_app.models.competition import Competition
from competitie_manager_app.models.team import Team
from competitie_manager_app.models.team_competition import TeamCompetition
from competitie_manager_app.forms.competition_form import CompetitionCreateForm


class CreateCompetitionView(LoginRequiredMixin, CreateView):
    login_url = '/login'
    redirect_field_name = 'competition_detail.html'
    template_name = 'competition_create.html'

    model = Competition
    form_class = CompetitionCreateForm

    def form_valid(self, form):
        form.instance.made_by = self.request.user
        redirect_url = super(CreateCompetitionView, self).form_valid(form)

        comp_teams = Team.objects.filter(
            sport_soort=form.instance.sport_soort).order_by('?')[:12]

        # .filter(competition__isnull=True)

        for team in comp_teams:
            team.competition.add(form.instance)

        return redirect_url
