"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "usuario"


urlpatterns = [
    path('entrar/',views.login_views,name = "loginpagina"),
    path('cadastro/',views.cadastro_views,name="cadastropagina"),
    path('logout/',views.logout_view,name='logout'),
    path('adicionar-imagem/',views.adiciona_views,name='adicionar_imagem'),
    path('apagar-imagem/',views.apaga_views,name='apaga_imagem'),
    path('editar-imagem/',views.edita_views,name='editar_imagem'),
    path('base/',views.base_views,name='basepagina')
]

urlpatterns += static(settings.MEDIA_URL,document_ROOT=settings.MEDIA_ROOT)