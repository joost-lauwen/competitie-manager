from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from competitie_manager_app.models.team import Team
from competitie_manager_app.forms.team_form import TeamForm

class CreateTeamView(LoginRequiredMixin, CreateView):
    login_url = '/login'
    redirect_field_name = 'team_detail.html'
    template_name = 'team_create.html'

    model = Team
    form_class = TeamForm

    def form_valid(self, form):
        form.instance.made_by = self.request.user
        return super(CreateTeamView, self).form_valid(form)
