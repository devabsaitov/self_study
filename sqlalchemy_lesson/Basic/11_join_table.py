from sqlalchemy import create_engine, Table, MetaData, column, Column, Integer, String, ForeignKey, select

engine = create_engine('postgresql://postgres:1@localhost/news_db')

meta = MetaData()
students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('first_name', String),
    Column('last_name', String)
)

mentor = Table(
    'mentors' , meta ,
    Column('id' , Integer , primary_key=True),
    Column('name' , String)

)

addresses = Table(
    'address', meta,
    Column('id', Integer, primary_key=True),
    Column('st_id', Integer, ForeignKey('students.id')),
    Column('mt_id', Integer, ForeignKey('mentors.id')),
    Column('name', String),
    Column('email', String)
)

meta.create_all(engine)

conn = engine.connect()

adres_mentor = addresses.join(mentor)
query = adres_mentor.join(students)

print_field = select([students.c.first_name, addresses.c.name , mentor.c.name]).select_from(query)

print(conn.execute(print_field).fetchall())

