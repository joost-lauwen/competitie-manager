from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from competitie_manager_app.models.match import Match
from competitie_manager_app.models.team_competition import TeamCompetition
from competitie_manager_app.forms.match_form import MatchUpdateForm

class MatchUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    redirect_field_name = 'match_detail.html'
    model = Match

    def get_form_class(self):
        return MatchUpdateForm

    def form_valid(self, form):
        home_goals = form.instance.h_goals
        away_goals = form.instance.a_goals

        home_team_competition = TeamCompetition.objects.filter(competition=form.instance.competition, team=form.instance.home_team).first()
        away_team_competition = TeamCompetition.objects.filter(competition=form.instance.competition, team=form.instance.away_team).first()
        print(home_team_competition)
        print(away_team_competition)

        form.instance.is_finished = True

        if home_goals > away_goals:
            form.instance.result = 1
            TeamCompetition.objects.filter(competition=form.instance.competition, team=form.instance.home_team).update(points=home_team_competition.points + 3)

        elif away_goals > home_goals:
            form.instance.result = 3

            TeamCompetition.objects.filter(competition=form.instance.competition, team=form.instance.away_team).update(points=away_team_competition.points + 3)

        else:
            form.instance.result = 2

            TeamCompetition.objects.filter(competition=form.instance.competition, team=form.instance.home_team).update(points=home_team_competition.points + 1)
            TeamCompetition.objects.filter(competition=form.instance.competition, team=form.instance.away_team).update(points=away_team_competition.points + 1)

        return super(MatchUpdateView, self).form_valid(form)
