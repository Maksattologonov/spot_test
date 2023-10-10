from common.exceptions import ObjectNotFoundException
from .models import Formula


class FormulaService:
    model = Formula

    @classmethod
    def get(cls, **filters):
        try:
            return cls.model.objects.filter(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException("Formula not found")

    @classmethod
    def filter_eduction(cls, **filters):
        return cls.model.objects.filter(**filters)

    @classmethod
    def save(cls, formula: str) -> Formula:
        return cls.model.objects.get_or_create(formula=formula)
