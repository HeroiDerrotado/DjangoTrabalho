from django.contrib import admin
from vidamarinha.models import Curiosidade

# Register your models here.

class CuriosidadeAdmin(admin.ModelAdmin):
    list_display = ('id','nome','legenda','publicada')
    list_display_links= ('id','nome')
    search_fields= ('nome',)
    list_filter = ('categoria',)
    list_editable =('publicada',)
    list_per_page = 10

admin.site.register(Curiosidade,CuriosidadeAdmin)    
