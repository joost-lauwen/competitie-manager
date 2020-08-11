from django.views.generic import DetailView
from competitie_manager_app.models.competition import Competition

# Class that handles the detailpage of a painting.
class CompetitionDetailView(DetailView):
    model = Competition
    context_object_name = 'competition_detail'
    template_name = 'competition_detail.html'
