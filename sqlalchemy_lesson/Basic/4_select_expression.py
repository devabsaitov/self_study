from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Numeric, text

engine = create_engine('postgresql://postgres:1@localhost/news_db', echo = True)

meta = MetaData()   # box

students = Table(
    'students' , meta ,
    Column('id' , Integer , primary_key=True),
    Column('first_name' , String),
    Column('last_name' , String)
)

user = Table(
    'users' , meta ,
    Column('id' , Integer , primary_key=True),
    Column('fullname' , String),
    Column('money' , Numeric)
)

meta.create_all(engine)

# -----------------------------------------------------
conn = engine.connect()
query_student = students.select()
students_data = conn.execute(query_student).fetchall()

for i in students_data:
    print(i.first_name)
