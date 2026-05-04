import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="centro_capacitacion",
        user="postgres",
        password="123"
    )