from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from competitie_manager_app.models.match import Match
from competitie_manager_app.models.competition import Competition

# Class to render the list page of matches model
class MatchListView(ListView):
    context_object_name = 'match_list'
    model = Match
    template_name = 'match_overview.html'

    def get_queryset(self):
        if self.kwargs == 'all':
            return Match.objects.all().order_by('-id')
        else:
            self.competitie = get_object_or_404(Competition, naam=self.kwargs['competitie'])

            return Match.objects.filter(competition=self.competitie)
