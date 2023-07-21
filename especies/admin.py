from django.contrib import admin
from especies.models import Imagem

# Register your models here.

class EspeciesAdmin(admin.ModelAdmin):
    list_display = ('id','nome','legenda','publicada')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_filter =  ('categoria',)
    list_editable = ('publicada',)
    list_per_page = 10

admin.site.register(Imagem,EspeciesAdmin)