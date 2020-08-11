from django.contrib import admin
from competitie_manager_app.models.sport import Sport
from competitie_manager_app.models.competition import Competition
from competitie_manager_app.models.team import Team

# Register your models here.
admin.site.register(Sport)
admin.site.register(Competition)
admin.site.register(Team)
