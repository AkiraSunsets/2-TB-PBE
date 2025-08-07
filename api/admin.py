from django.contrib import admin

from .models import * #asterisco importa todos os modelos

admin.site.register(Autor) #Registra o modelo Autor no site de administração do Django

