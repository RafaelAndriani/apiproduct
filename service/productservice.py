import repository.database as db
from model.product import Product


def find_all():
    columns = db.select_all_products()
    return convert_product_list(columns)


def find_custom(column, value):
    columns = db.select_by_column(column, value)
    return convert_product_list(columns)


def save(product):
    if not check_duplicate(product.id):
        return False
    db.save_product(product)
    return True


def delete(id):
    delete_confirmation = db.delete_product(id)
    return delete_confirmation


def update(product):
    return db.update_product(id=product.id, name=product.name, price=product.price)


def check_duplicate(id_check):
    if not db.select_by_column(column="id", value=id_check):
        return True
    else:
        return False


def convert_product_list(columns):
    product_list = []
    for c in columns:
        product_list.append(Product(c[0], c[1], c[2]))
    return product_list
