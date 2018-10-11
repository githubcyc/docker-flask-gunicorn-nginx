
import dataset
# https://dataset.readthedocs.io/en/latest/quickstart.html#connecting-to-a-database
# connecting to a SQLite database
# db = dataset.connect('sqlite:///mydatabase.db')

# connecting to a MySQL database with user and password
# export DATABASE_URL=
# http://docs.sqlalchemy.org/en/latest/dialects/mysql.html#module-sqlalchemy.dialects.mysql.pymysql
# dialect://user:password@host/dbname
# mysql+pyodbc
db = dataset.connect('mysql+pymysql://root:123@localhost/test?charset=utf8')

# connecting to a PostgreSQL database
# db = dataset.connect('postgresql://scott:tiger@localhost:5432/mydatabase')

# get a reference to the table 'user'
table = db['user']

# Insert a new record.
# table.insert(dict(name='John Doe', age=3, country='China'))

# dataset will create "missing" columns any time you insert a dict with an unknown key
# table.insert(dict(name='Jane Doe', age=37, country='France', gender='female'))

# UPDATE test SET age=5 WHERE name="John Doe"; 
# table.update(dict(name='John Doe', age=5), ['name'])

# Using Transactions
# with db as tx:
#     tx['user'].insert(dict(name='John Doe', age=46, country='China'))


print(db.tables)
print(db['user'].columns)
print(len(db['user']))

users = db['user']
for u in users:
    print(u)

