from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from competitie_manager_app.models.competition import Competition
from competitie_manager_app.forms.competition_form import CompetitionCreateForm


class CreateCompetitionView(LoginRequiredMixin, CreateView):
    login_url = '/login'
    redirect_field_name = 'competition_detail.html'
    template_name = 'competition_create.html'

    model = Competition
    form_class = CompetitionCreateForm

    def form_valid(self, form):
        form.instance.made_by = self.request.user
        return super(CreateCompetitionView, self).form_valid(form)
