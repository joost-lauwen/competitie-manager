from django.views.generic import ListView
from competitie_manager_app.models.match import Match
from competitie_manager_app.models.competition import Competition
from competitie_manager_app.models.bet import Bet
from competitie_manager_app.models.team_competition import TeamCompetition
from competitie_manager_app.models.user_toto_info import UserTotoInfo
from competitie_manager_app.models.team import Team

# Class to render the user dashboard view
class UserDashboardView(ListView):
    context_object_name = 'user_dashboard'
    model = Bet
    template_name = 'user_dashboard.html'

    def get_queryset(self):
        return Bet.objects.filter(user=self.request.user).order_by('-id')[:10]

    # Get the necesarry date to show on the dashboard page
    def get_context_data(self, **kwargs):
        context = super(UserDashboardView, self).get_context_data(**kwargs)
        context['match_list'] = Match.objects.all().order_by('-id')[:5]
        context['competition_list'] = Competition.objects.all().order_by('-id')[:5]
        context['team_list'] = Team.objects.all().order_by('-id')[:5]
        context['toto_ranking'] = UserTotoInfo.objects.all().order_by('-toto_points')[:10]
        context['user_toto_ranking'] = UserTotoInfo.objects.get(user=self.request.user)

        return context
