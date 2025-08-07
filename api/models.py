from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255) #NULL significa que o campo pode ser nulo
    nasc = models.DateField(null=True, blank=True) #DateField campo de data
    nacion = models.CharField(max_length=30, null=True, blank=True) # CharField campo de caracteres limitado
    bio = models.TextField(null=True, blank =True) #TextField não tem limite de caracteres

    def __str__(self):
        return f"{self.nome} {self.sobrenome}" #Representação em string do modelo Autor
    