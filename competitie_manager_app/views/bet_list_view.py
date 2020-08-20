from django.views.generic import ListView
from competitie_manager_app.models.bet import Bet

# Class to render list page of bets
class BetListView(ListView):
    context_object_name = 'bet_list'
    model = Bet
    template_name = 'bet_overview.html'
    paginate_by = 10

    def get_queryset(self):
        return Bet.objects.filter(user=self.request.user).order_by('-id')
