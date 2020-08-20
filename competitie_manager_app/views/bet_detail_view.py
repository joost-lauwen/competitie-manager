from django.views.generic import DetailView
from competitie_manager_app.models.bet import Bet

# Class to render detail page of a bet
class BetDetailView(DetailView):
    model = Bet
    context_object_name = 'bet_detail'
    template_name = 'bet_detail.html'
