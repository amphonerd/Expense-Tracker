import psycopg2


def get_connection():

    connection = psycopg2.connect(
        dbname="expense_db",
        user="postgres",
        password="YOUR_PASSWORD",
        host="localhost",
        port="5432",
    )
    return connection


def create_tables(connection):
    f = open("schema.sql")
    sql = f.read()
    f.close()

    cur = connection.cursor()
    cur.execute(sql)
    connection.commit()
    cur.close()
