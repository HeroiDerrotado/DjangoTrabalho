from django.contrib import admin
from pesca.models import Pesca

#Register your models here.

class PescaAdmin(admin.ModelAdmin):
    list_display = ('id','nome','legenda','publicada')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_filter = ('categoria',) #'usuario')
    lista_editable = ('publicada',)
    list_per_page = 10

admin.site.register(Pesca,PescaAdmin)    
