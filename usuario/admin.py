from django.contrib import admin
from usuario.models import Usuario

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id','nome','legenda','publicada')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_filter = ('categoria','usuario')
    lista_editable = ('publicada',)
    list_per_page = 10

admin.site.register(Usuario,UsuarioAdmin)    

