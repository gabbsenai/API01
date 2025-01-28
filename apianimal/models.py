from django.db import models

class animal(models.Model):
    nome = models.CharField(max_length=30)
    tutor = models.CharField(max_length=50)

    def __str__(self):
        return self.nome