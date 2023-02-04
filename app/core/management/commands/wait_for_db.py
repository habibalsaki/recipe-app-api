"""
Django command to wait for the database to be available
"""
import time 

from typing import Any, Optional
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError

class Command(BaseCommand):
    """Django command to wait for the database

    Args:
        BaseCommand (_type_): _description_
    """

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        """Entry point for the command

        Returns:
            Optional[str]: _description_
        """
        self.stdout.write("Waiting for database")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write("Database unavailable, wait for 1 second")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database Available'))
