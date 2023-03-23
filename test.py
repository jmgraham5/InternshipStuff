import sqlite3

container = sqlite3.connect('mydb_justin')
c = container.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS products
    ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT)
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS prices
    ([product_id] INTEGER PRIMARY KEY, [price] INTEGER)
''')

container.commit()
