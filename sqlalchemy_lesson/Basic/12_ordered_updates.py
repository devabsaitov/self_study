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
    'addresses', meta,
    Column('id', Integer, primary_key=True),
    Column('st_id', Integer, ForeignKey('students.id')),
    Column('name', String),
    Column('email', String)
)

conn = engine.connect()
query = students.update().values([(students.c.first_name, 'PDP'),(students.c.last_name , students.c.first_name + 'absd')]).where(students.c.id > 6)
conn.execute(query)