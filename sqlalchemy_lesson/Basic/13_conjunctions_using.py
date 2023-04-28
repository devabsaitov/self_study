from operator import not_

from sqlalchemy import create_engine, Table, MetaData, column, Column, Integer, String, ForeignKey, select, and_, or_

engine = create_engine('postgresql://postgres:1@localhost/news_db')

meta = MetaData()
students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('first_name', String),
    Column('last_name', String)
)

addresses = Table(
    'addresses', meta,
    Column('id', Integer, primary_key=True),
    Column('st_id', Integer, ForeignKey('students.id')),
    Column('postal', String),
    Column('email', String)
)

conn = engine.connect()

# query = addresses.delete().where(students.c.id > 14).where(students.c.id == addresses.c.st_id).where(addresses.c.email.startswith('te%'))
query = students.delete().where(and_(students.c.id > 3 , students.c.id < 6))
a = conn.execute(query).fetchall()
print(a)