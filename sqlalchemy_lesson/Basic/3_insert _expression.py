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
student2 = text("insert into students(first_name , last_name) values ('jahongir' , 'Abdushukurov')")
# student1 = students.insert().values(first_name = 'Botirjon' , last_name = 'Botiraliyev')
# user1 = user.insert().values(fullname = 'Absaitov Dilshod' , money = 10_000)
conn.execute(student2)

