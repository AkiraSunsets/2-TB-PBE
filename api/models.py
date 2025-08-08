from django.db import models

class Autor(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255) #NULL significa que o campo pode ser nulo
    birth_date = models.DateField(null=True, blank=True) #DateField campo de data
    nacionality = models.CharField(max_length=30, null=True, blank=True) # CharField campo de caracteres limitado
    biografy = models.TextField(null=True, blank =True) #TextField não tem limite de caracteres

    def __str__(self):
        return f"{self.name} {self.last_name}" #Representação em string do modelo Autor

class Book(models.Model): #cria o campinho do Book bem de cria 
    title = models.CharField(max_length=255)
    realese_date = models.DateField(null=True, blank=True)
    autor = models.CharField(max_length=255)
    pages = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} {self.autor}" #Representação em string do modelo Book