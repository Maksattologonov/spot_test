import logging


class ExcludeSessionSQLFilter(logging.Filter):
    def filter(self, record):
        return 'django.contrib.sessions' not in record.getMessage()
