import psycopg2
from model.client import Client

conn = psycopg2.connect(
    database="postgres", user='postgres', password='admin', host='127.0.0.1', port='5432'
)

cursor = conn.cursor()


def select_by_column(column, value):
    cursor.execute(f'select "cnpj", "name", "address" from client where "{column}" = \'{value}\'')
    data = cursor.fetchall()
    count = cursor.rowcount
    print(count, "Clients founded by:select_by_column")
    return data


def select_all_clients():
    sql = 'select "cnpj", "name", "address" from client'
    cursor.execute(sql)
    data = cursor.fetchall()
    count = cursor.rowcount
    print(count, "Clients founded by:select_all_clients")
    return data


def save_client(client):
    """query sql"""
    sql = f'INSERT INTO public.client (cnpj, \"name\", address) VALUES(\'{client.cnpj}\', \'{client.name}\',' \
          f' \'{client.address}\'); '
    cursor.execute(sql)
    conn.commit()
    count = cursor.rowcount
    print(count, "Record successfully inserted into the database")


def delete_client(cnpj):
    sql = f'DELETE FROM public.client WHERE cnpj=\'{cnpj}\''
    cursor.execute(sql)
    conn.commit()
    count = cursor.rowcount
    print(count, "Successfully delete from database")


def update_client(cnpj, name, address):
    sql = f'UPDATE public.client SET "name"=\'{name}\', address=\'{address}\' WHERE cnpj=\'{cnpj}\''
    cursor.execute(sql)
    conn.commit()
    count = cursor.rowcount
    print(count, "Successfully update from database")



