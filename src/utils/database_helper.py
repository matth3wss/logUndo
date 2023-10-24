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
        conn.autocommit = True
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def create_table(cursor):
    cursor.execute('DROP TABLE IF EXISTS data;')
    try:
        cursor.execute('''
                    CREATE TABLE data (
                        id INTEGER NOT NULL,
                        A INTEGER NOT NULL,
                        B INTEGER NOT NULL
                    );
                    ''')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def load_data(cursor, json_data):
    ids = json_data['table']['id']
    column_a = json_data['table']['A']
    column_b = json_data['table']['B']

    for i in range(len(ids)):
        cursor.execute('''
                       INSERT INTO data (id, A, B)
                       VALUES (%s, %s, %s);
                       ''', (ids[i], column_a[i], column_b[i]))
