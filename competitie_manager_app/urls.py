from django.urls import path
from django.contrib.auth import views as auth_views
from competitie_manager_app import views

app_name = 'competitie_manager_app'

urlpatterns = [
    path('',
        views.index_view.HomePage.as_view(),
        name='index'),
    path('inloggen/',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login'),
    path('uitloggen/',
        auth_views.LogoutView.as_view(),
        name='logout'),
    path('registreren/',
        views.register_view.SignUp.as_view(),
        name='signup'),
    path('teammaken/',
        views.CreateTeamView.as_view(),
        name='create_team'),
    path('team/<int:pk>/',
        views.TeamDetailView.as_view(),
        name='team_detail'),
    path('competitiemaken/',
        views.CreateCompetitionView.as_view(),
        name='create_competition'),
    path('competition/<int:pk>/',
        views.CompetitionDetailView.as_view(),
        name='competition_detail'),
    path('competities/',
        views.competition_list_view.CompetitionListView.as_view(),
        name='competition_list'),
    path('<competitie>/wedstrijden',
        views.match_list_view.MatchListView.as_view(),
        name='matches'),
    path('<competitie>/wedstrijden/<int:pk>/',
        views.match_detail_view.MatchDetailView.as_view(),
        name='match_detail'),
    path('<competitie>/wedstrijden/<int:pk>/uitslag_invullen',
        views.match_update_view.MatchUpdateView.as_view(),
        name='match_update'),
]
