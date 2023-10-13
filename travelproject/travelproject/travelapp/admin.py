from django.contrib import admin

# Register your models here.
from . models import Place1
admin.site.register(Place1)

from . models import Team
admin.site.register(Team)