from django.db import models


class Clothes(models.Model):
    type_type = models.CharField("Tipo de roupa", max_length=255, blank = True, null = True)
    cloth = models.CharField("Tecido", max_length=255, blank = True, null = True)
    size = models.CharField("tamanho", max_length=255, blank = True, null = True)
    cor = models.CharField("color", max_length=20, blank = True, null = True)
   
    class Meta:
        verbose_name_plural = 'Clothes'

    def __str__(self):
        return self.type_type
