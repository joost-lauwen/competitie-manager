from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from competitie_manager_app.models.competition import Competition
from competitie_manager_app.models.team import Team
from competitie_manager_app.models.team_competition import TeamCompetition
from competitie_manager_app.models.match import Match
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

        round_robin_teams = list(comp_teams)

        rounds = (len(round_robin_teams) - 1) * 2
        matches = CreateCompetitionView.round_robin(round_robin_teams, rounds)

        for round in matches:

            for match in round:
                home_team = match[0]
                away_team = match[1]

                if home_team is None:
                    pass
                elif away_team is None:
                    pass
                else:
                    Match.objects.create(
                        home_team=home_team, away_team=away_team, competition=form.instance)

        return redirect_url

    def round_robin(teams, rounds):

        if len(teams) % 2:
            teams.append(None)

        schedule = []

        for turn in range(rounds):
            pairings = []

            for i in range(len(teams) // 2):
                if turn % 2:
                    home = teams[i]
                    away = teams[len(teams) - i - 1]
                else:
                    home = teams[len(teams) - i - 1]
                    away = teams[i]
                pairings.append((home, away))

            teams.insert(1, teams.pop())
            schedule.append(pairings)

        return schedule
