from rest_framework import serializers #serializers transforma o arquivo em json
from .models import Autor, Book

class AutorSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Autor 
        fields = '__all__' #seleciona todos os campos do model Autor

class BookSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Book
        fields = '__all__' #seleciona todos os campos do model Book
