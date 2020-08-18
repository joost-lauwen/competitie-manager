from django.views.generic import ListView
from competitie_manager_app.models.match import Match


class MatchAllListView(ListView):
    context_object_name = 'match_all_list'
    model = Match
    template_name = 'match_all_overview.html'

    def get_queryset(self):
        return Match.objects.all().order_by('-id')
