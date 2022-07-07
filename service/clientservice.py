import repository.database as db
from model.client import Client


def find_all():
    columns = db.select_all_clients()
    return convert_client_list(columns)


def find_custom(column, value):
    columns = db.select_by_column(column, value)
    return convert_client_list(columns)


def save(client):
    if not check_duplicate(client.cnpj):
        return False
    if has_numbers(client.name):
        return False
    db.save_client(client)
    return True


def delete(cnpj):
    delete_confirmation = db.delete_client(cnpj)
    return delete_confirmation


def update(client):
    return db.update_client(cnpj=client.cnpj, name=client.name, address=client.address)


def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


def check_duplicate(cnpj_check):
    if not db.select_by_column(column="cnpj", value=cnpj_check):
        return True
    else:
        return False


def convert_client_list(columns):
    client_list = []
    for c in columns:
        client_list.append(Client(c[0], c[1], c[2]))
    return client_list
