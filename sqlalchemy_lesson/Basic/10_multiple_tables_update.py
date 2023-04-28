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
    Column('st_id', Integer, ForeignKey('students.id')),
    Column('name', String),
    Column('email', String)
)

conn = engine.connect()
query = students.update().values([{students.c.first_name:'komila'}]).where(students.c.id == addresses.c.st_id)
# query = addresses.update().values({ addresses.c.email:'komila@gmail.com'}).where(students.c.id == addresses.c.id)
conn.execute(query)