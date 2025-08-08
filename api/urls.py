from django.urls import path

from .views import * # Importa todas as views do módulo

urlpatterns = [ #paleta de endpoints
    path('autores/', AutoresView.as_view()),
    path('books/', BooksView.as_view()),
]