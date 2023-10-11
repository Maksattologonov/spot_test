from django.db import models


class Formula(models.Model):
    formula = models.CharField(max_length=255, verbose_name='Формула')

    def __str__(self):
        return self.formula

    class Meta:
        verbose_name = 'Формула'
        verbose_name_plural = 'Формулы'


class QueryLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    source_ip = models.GenericIPAddressField()
    input_data = models.TextField()
    result = models.BooleanField()
