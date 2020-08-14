from django.views.generic import DetailView
from competitie_manager_app.models.bet import Bet


class BetDetailView(DetailView):
    model = Bet
    context_object_name = 'bet_detail'
    template_name = 'bet_detail.html'
