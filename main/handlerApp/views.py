from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .apis import FormulaSerializer
from .services import FormulaService


class FormulaAPIView(APIView):

    def get(self, request, *args, **kwargs):
        instance = FormulaService.get()
        serializer = FormulaSerializer(instance, many=True)
        return Response(serializer.data)