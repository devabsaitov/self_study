from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, text

engine = create_engine('postgresql://postgres:1@localhost/news_db')

meta = MetaData()
students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('lastname', String))

conn = engine.connect()

del_query = students.delete().where(students.c.id == 2)
conn.execute(del_query)

# print(list(conn.execute(text('select * from students;'))))
