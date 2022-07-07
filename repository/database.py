import psycopg2

conn = psycopg2.connect(
    database="postgres", user='postgres', password='admin', host='127.0.0.1', port='5432'
)

cursor = conn.cursor()


def select_by_column(column, value):
    cursor.execute(f'select "id", "name", "price" from product where "{column}" = \'{value}\'')
    data = cursor.fetchall()
    count = cursor.rowcount
    if count >= 1:
        print(count, "Products founded by:select_by_column")
        return data
    else:
        return False


def select_all_products():
    sql = 'select "id", "name", "price" from product'
    cursor.execute(sql)
    data = cursor.fetchall()
    count = cursor.rowcount
    print(count, "Products founded by:select_all_products")
    return data


def save_product(product):
    sql = f'INSERT INTO public.product (id, \"name\", price) VALUES(\'{product.id}\', \'{product.name}\',' \
          f' \'{product.price}\'); '
    cursor.execute(sql)
    conn.commit()
    count = cursor.rowcount
    print(count, "Record successfully inserted into the database")


def delete_product(product):
    sql = f'DELETE FROM public.product WHERE id=\'{product}\''
    cursor.execute(sql)
    conn.commit()
    count = cursor.rowcount
    return count == 1


def update_product(id, name, price):
    sql = f'UPDATE public.product SET "name"=\'{name}\', price={price} WHERE id={id}'
    cursor.execute(sql)
    conn.commit()
    count = cursor.rowcount
    return count == 1


def id_list():
    sql = "select id from product;"
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.commit()
    return data
