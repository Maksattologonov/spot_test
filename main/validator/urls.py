from django.urls import path
from .views import FormulaAPIView, FormulaValidationAPIView

urlpatterns = [
    path('formula/', FormulaAPIView.as_view(), name='formula'),
    path('formula_validation/', FormulaValidationAPIView.as_view(), name='formula-validation'),
    ]
