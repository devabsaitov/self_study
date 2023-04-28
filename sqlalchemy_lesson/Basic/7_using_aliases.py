from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, select

engine = create_engine('postgresql://postgres:1@localhost/news_db')

meta = MetaData()

students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('first_name', String),
    Column('last_name', String))

# meta.create_all(engine)

conn = engine.connect()

st = students.alias()
s = st.select().where(st.c.id > 2)
result = conn.execute(s).fetchall()
print(result)
