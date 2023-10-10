from django.db import models


class Formula(models.Model):
    formula = models.CharField(max_length=255, verbose_name='Формула')

    def __str__(self):
        return self.formula

    class Meta:
        verbose_name = 'Формула'
        verbose_name_plural = 'Формулы'
        