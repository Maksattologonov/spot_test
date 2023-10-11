import logging

from common.exceptions import ObjectNotFoundException
from .models import Formula, QueryLog

logger = logging.getLogger('django.db.backends')


class FormulaService:
    model = Formula

    @classmethod
    def get(cls, **filters):
        try:
            result = cls.model.objects.filter(**filters)
            return result
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException("Formula not found")

    @classmethod
    def filter_eduction(cls, **filters):
        return cls.model.objects.filter(**filters)

    @classmethod
    def save(cls, formula: str) -> Formula:
        return cls.model.objects.get_or_create(formula=formula)


class QueryLogService:
    model = QueryLog

    @classmethod
    def save(cls, source_ip: str, input_data: str, result: bool):
        stmt = cls.model.objects.create(
                                        source_ip=source_ip,
                                        input_data=input_data,
                                        result=result
                                        )
        return stmt
