from django.urls import path
from .views import FormulaAPIView

urlpatterns = [
    path('formula/', FormulaAPIView.as_view(), name='formula'),
    ]
