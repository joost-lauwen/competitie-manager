from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from competitie_manager_app.models.bet import Bet
from competitie_manager_app.models.match import Match
from competitie_manager_app.forms.bet_form import BetCreateForm


class CreateBetView(LoginRequiredMixin, CreateView):
    login_url = '/login'
    redirect_field_name = 'bet_detail.html'
    template_name = 'bet_create.html'

    model = Bet
    form_class = BetCreateForm


    def get_succes_url(self):
        return reverse('bet_detail', kwargs={"competitie": self.match.competition, "match_pk": self.match, "pk": self.object.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        match = Match.objects.get(pk=self.kwargs['match_pk'])
        form.instance.match = match
        form.instance.quotation_h_team = Bet.get_quotation_h_team(form.instance)
        form.instance.quotation_a_team = Bet.get_quotation_a_team(form.instance)
        form.instance.quotation_draw = Bet.get_quotation_draw(form.instance)

        redirect_url = super(CreateBetView, self).form_valid(form)

        return redirect_url
