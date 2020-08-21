from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from competitie_manager_app.models.bet import Bet
from competitie_manager_app.models.match import Match
from competitie_manager_app.forms.bet_form import BetCreateForm
from competitie_manager_app.models.user_toto_info import UserTotoInfo

# Class to render create view of the bet model
class CreateBetView(LoginRequiredMixin, CreateView):
    login_url = '/login'
    redirect_field_name = 'bet_detail.html'
    template_name = 'bet_create.html'

    model = Bet
    form_class = BetCreateForm

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user

        return kwargs

    def get_succes_url(self):
        return reverse('bet_detail', kwargs={"competitie": self.match.competition, "match_pk": self.match, "pk": self.object.pk})

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user

        match = Match.objects.get(pk=self.kwargs['match_pk'])

        # Get the quotations for the match
        form.instance.match = match
        form.instance.quotation_h_team = Bet.get_quotation_h_team(
            form.instance)
        form.instance.quotation_a_team = Bet.get_quotation_a_team(
            form.instance)
        form.instance.quotation_draw = Bet.get_quotation_draw(form.instance)

        user_toto_points = UserTotoInfo.objects.get(user=user).toto_points
        new_user_toto_points = user_toto_points - form.instance.stake

        UserTotoInfo.objects.filter(user=user).update(
            user=user, toto_points=new_user_toto_points)

        redirect_url = super(CreateBetView, self).form_valid(form)

        return redirect_url

    def get_context_data(self, **kwargs):
        context = super(CreateBetView, self).get_context_data(**kwargs)
        context['match'] = Match.objects.get(pk=self.kwargs['match_pk'])

        return context
