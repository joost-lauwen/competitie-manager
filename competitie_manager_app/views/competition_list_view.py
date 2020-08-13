from django.views.generic import ListView
from competitie_manager_app.models.competition import Competition

class CompetitionListView(ListView):
    context_object_name = 'competition_list'
    model = Competition
    template_name = 'competition_overview.html'

    def get_queryset(self):
        return Competition.objects.order_by('naam')
