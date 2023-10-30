import psycopg2
from core.settings import settings
from utils.json_helper import extract_keys, extract_values, extract_table_name


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


def create_table(con, json_data):
    cursor = con.cursor()

    table_name = extract_table_name(json_data)
    cursor.execute(f'DROP TABLE IF EXISTS {table_name};')

    columns = extract_keys(json_data)
    columns = ', '.join(
        [f'{column} INTEGER NOT NULL' for column in columns])
    # columns = str(columns)
    try:
        cursor.execute(f'''CREATE TABLE {table_name} ({columns});''')
        con.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return columns

