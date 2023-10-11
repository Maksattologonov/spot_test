from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .apis import FormulaSerializer, FormulaValidationSerializer
from .models import QueryLog
from .services import FormulaService, QueryLogService


class FormulaAPIView(APIView):

    def get(self, request, *args, **kwargs):
        instance = FormulaService.get()
        serializer = FormulaSerializer(instance, many=True)
        return Response(serializer.data)


class FormulaValidationAPIView(APIView):
    def post(self, request):
        serializer = FormulaValidationSerializer(data=request.data)
        if serializer.is_valid():
            formula = serializer.validated_data['formula']
            is_valid = self.validate_formula(formula)
            QueryLogService.save(source_ip=request.META.get('REMOTE_ADDR'),
                                 input_data=str(request.data),
                                 result=is_valid)
            return Response(is_valid)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def validate_formula(self, formula):
        stack = []
        opening_brackets = "([{"
        closing_brackets = ")]}"
        bracket_pairs = {')': '(', ']': '[', '}': '{'}

        for char in formula:
            if char in opening_brackets:
                stack.append(char)
            elif char in closing_brackets:
                if not stack or stack.pop() != bracket_pairs[char]:
                    return False

        if any(char in formula for char in opening_brackets) and any(char in formula for char in closing_brackets):
            return True
        else:
            return False
