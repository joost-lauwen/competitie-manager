from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from competitie_manager_app.models.competition import Competition
from competitie_manager_app.models.team import Team
from competitie_manager_app.models.team_competition import TeamCompetition
from competitie_manager_app.models.match import Match
from competitie_manager_app.forms.competition_form import CompetitionCreateForm

# Class to render the creation page of the competition model
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

        for team in comp_teams:
            team.competition.add(form.instance)

        # Convert query to list
        round_robin_teams = list(comp_teams)

        # Calculate the rounds for a home and away game
        rounds = (len(round_robin_teams) - 1) * 2

        # Create the competition matches
        matches = CreateCompetitionView.round_robin(round_robin_teams, rounds)

        for round in matches:

            for match in round:
                home_team = match[0]
                away_team = match[1]

                Match.objects.create(
                    home_team=home_team, away_team=away_team, competition=form.instance)

                # if home_team is None or away_team is None:
                #     raise ValidationError(
                #         "Er is een oneven aantal teams voor de gekozen sport."
                #         "Voeg een team toe voor de gekozen sport of kies een andere sport om een competitie voor aan te maken."
                #     )
                # else:
                #     Match.objects.create(
                #         home_team=home_team, away_team=away_team, competition=form.instance)

        return redirect_url

    def round_robin(teams, rounds):

        # Add None to teams if there is an uneven amount of teams
        if len(teams) % 2:
            teams.append(None)

        schedule = []

        # Loop to create pairings for each round
        for turn in range(rounds):
            pairings = []

            # Loop to determine home and away team for each round
            for i in range(len(teams) // 2):
                # If round is an odd number put the home teams as home team
                if turn % 2:
                    home = teams[i]
                    away = teams[len(teams) - i - 1]
                # Else put the home team as away team
                else:
                    home = teams[len(teams) - i - 1]
                    away = teams[i]
                    # Pair the home and away team to the list
                pairings.append((home, away))

            teams.insert(1, teams.pop())
            # Append all the pairings to the schedule list
            schedule.append(pairings)

        # Return the created schedule
        return schedule
