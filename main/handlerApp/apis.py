from rest_framework import serializers
from .models import Formula


class FormulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formula
        fields = ('formula',)