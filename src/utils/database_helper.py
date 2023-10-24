import psycopg2
from core.settings import settings


def create_connection():
    try:
        conn = psycopg2.connect(
            host=settings.DATABASE_HOST,
            database=settings.DATABASE_NAME,
            user=settings.DATABASE_USER,
            password=settings.DATABASE_PASSWORD,
            port=settings.DATABASE_PORT
        )
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def create_table(cursor):
    cursor.execute('''
                   CREATE TABLE table(
                       id SERIAL PRIMARY KEY,
                       A INTEGER NOT NULL,
                       B INTEGER NOT NULL
                   );
                   ''')

