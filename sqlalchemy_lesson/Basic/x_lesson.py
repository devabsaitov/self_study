from sqlalchemy import create_engine
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Numeric, text




engine = create_engine('postgresql://postgres:1@localhost/news_db', echo = True)

engine.connect()

meta = MetaData()
students = Table(
    'students' , meta ,
    Column('id' , Integer , primary_key=True),
    Column('first_name' , String),
    Column('last_name' , String)
)
conn = engine.connect()

query = students.update().values([(students.c.last_name, 'Aliyev') , (students.c.first_name , 'Botir')]).where(students.c.id == 3)
conn.execute(query)