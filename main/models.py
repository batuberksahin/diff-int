from django.db import models

class question(models.Model):
    value = models.CharField(max_length=256, verbose_name='Denklem')
    variable = models.CharField(max_length=10, verbose_name='Degişken')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Tarih')

    def __str__(self):
        return self.date