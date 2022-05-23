from atexit import register
from django.contrib import admin
from .models import *
# Register your models here.

#admin.site.register(Project)
admin.site.register(Famille)
admin.site.register(Activité)
admin.site.register(Perimetre)
admin.site.register(Champ)
admin.site.register(Region)
admin.site.register(Type)
admin.site.register(Structure)
admin.site.register(Fiscalite)
#admin.site.register(Prévision_mensuelle)
#admin.site.register(Realisation_mensuelle)
admin.site.register(Acces)
#admin.site.register(Recap_region)
#admin.site.register(Recap_famille)
#admin.site.register(Recap_activite)
#admin.site.register(Recap)
#admin.site.register(Stimulation)
#admin.site.register(Prévision_mensuelle_stimulation)