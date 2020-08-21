from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
import decimal
from competitie_manager_app.models.match import Match
from competitie_manager_app.models.team_competition import TeamCompetition
from competitie_manager_app.models.bet import Bet
from competitie_manager_app.models.user_toto_info import UserTotoInfo
from competitie_manager_app.forms.match_form import MatchUpdateForm


# Class to render and handle the update of a match model
class MatchUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    redirect_field_name = 'match_detail.html'
    model = Match

    def get_form_class(self):
        return MatchUpdateForm

    def form_valid(self, form):
        home_goals = form.instance.h_goals
        away_goals = form.instance.a_goals

        home_team_competition = TeamCompetition.objects.filter(
            competition=form.instance.competition, team=form.instance.home_team).first()
        away_team_competition = TeamCompetition.objects.filter(
            competition=form.instance.competition, team=form.instance.away_team).first()

        form.instance.is_finished = True

        # Determine match result and points each team has won
        if home_goals > away_goals:
            form.instance.result = 1
            TeamCompetition.objects.filter(competition=form.instance.competition, team=form.instance.home_team).update(
                points=home_team_competition.points + 3)

        elif away_goals > home_goals:
            form.instance.result = 3

            TeamCompetition.objects.filter(competition=form.instance.competition, team=form.instance.away_team).update(
                points=away_team_competition.points + 3)

        else:
            form.instance.result = 2

            # Update the amount of points each team has gained
            TeamCompetition.objects.filter(competition=form.instance.competition, team=form.instance.home_team).update(
                points=home_team_competition.points + 1)
            TeamCompetition.objects.filter(competition=form.instance.competition, team=form.instance.away_team).update(
                points=away_team_competition.points + 1)

        # Get bets for updated match
        bets = Bet.objects.filter(match=form.instance)

        # Update bet results for each bet for the updated match
        for bet in bets:
            if bet.gamble == form.instance.result:
                bet.bet_result = True
                if form.instance.result == 1:
                    bet.prize_amount = bet.stake * bet.quotation_h_team
                elif form.instance.result == 2:
                    bet.prize_amount = bet.stake * bet.quotation_draw
                else:
                    bet.prize_amount = bet.stake * bet.quotation_a_team
            else:
                bet.bet_result = False
                bet.prize_amount = 0

            # Update total toto points for each user who made a bet on the updated match
            user_toto_points = UserTotoInfo.objects.get(user=bet.user).toto_points
            UserTotoInfo.objects.filter(user=bet.user).update(user=bet.user, toto_points=user_toto_points + decimal.Decimal(bet.prize_amount))
            bet.save()

        return super(MatchUpdateView, self).form_valid(form)
