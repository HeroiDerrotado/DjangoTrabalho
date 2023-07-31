from django.contrib import admin
from usuario.models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    list_filter = ('username', 'email')
    search_fields = ('username', 'email')

admin.site.register(Usuario, UsuarioAdmin)
