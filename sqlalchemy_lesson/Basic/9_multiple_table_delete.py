from sqlalchemy import create_engine, Table, MetaData, column, Column, Integer, String, ForeignKey, select

engine = create_engine('postgresql://postgres:1@localhost/news_db')

meta = MetaData()
students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('first_name', String),
    Column('last_name', String)
)

addresses = Table(
    'address', meta,
    Column('id', Integer, primary_key=True),
    Column('st_id', Integer, ForeignKey('students.id')),
    Column('name', String),
    Column('email', String)
)

conn = engine.connect()

query = students.select().where(students.c.id > 4).where(students.c.id == addresses.c.st_id).where(addresses.c.email.startswith('te%'))
a = conn.execute(query).fetchall()
print(a)