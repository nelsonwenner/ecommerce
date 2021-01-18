from django.core.management.base import BaseCommand
from django.db import connection
from django.conf import settings

class Command(BaseCommand):

    def handle(self, **options):
        self.drop_tables()

    handle.short_description = u"Database reset"

    def drop_tables(self):
        cursor = connection.cursor()
        tables = connection.introspection.table_names()
        connection_driver = settings.DATABASES['default']['ENGINE']
        end_command = None
        if connection_driver == 'django.db.backends.sqlite3':
            cursor.execute('PRAGMA foreign_keys = OFF;')
            drop_table_command = 'DROP TABLE IF EXISTS %s;'
            end_command = 'PRAGMA foreign_keys = ON;'
        elif connection_driver == 'django.db.backends.postgresql':
            drop_table_command = 'DROP TABLE IF EXISTS %s CASCADE;'
        for table in tables:
            cursor.execute(drop_table_command % table)

        if end_command:
            cursor.execute(end_command)