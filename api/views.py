from django.shortcuts import render #render é de renderizar o template
from rest_framework.generics import ListCreateAPIView
from .models import Autor, Book 
from .serializers import AutorSerializers, BookSerializers

class AutoresView(ListCreateAPIView):
    queryset = Autor.objects.all() #retorna todos os autores
    serializer_class = AutorSerializers #utiliza o serializer AutorSerializers para transformar o model em json

class BooksView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

