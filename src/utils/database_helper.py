import psycopg2
import os
from core.settings import settings


def connect():
    try:
        conn = psycopg2.connect(
            host=settings.DATABASE_HOST,
            database=settings.DATABASE_NAME,
            user=settings.DATABASE_USER,
            password=settings.DATABASE_PASSWORD
        )
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
