from sqlalchemy import create_engine, Table, MetaData, column, Column, Integer, String, ForeignKey, select, func

engine = create_engine('postgresql://postgres:1@localhost/news_db')

meta = MetaData()
students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('lastname', String)
)

addresses = Table(
    'addresses', meta,
    Column('id', Integer, primary_key=True),
    Column('st_id', Integer, ForeignKey('students.id')),
    Column('postal', String),
    Column('email', String)
)


conn = engine.connect()
time_query = select([func.now()])                             # now() hozirgi vaqt
students_id = select([func.count(students.c.id)]).where(students.c.id == 21)
addresses_max_id = select([func.max(addresses.c.id)])
addresses_avg_id = select([func.avg(addresses.c.id)])         # avg() o'rta arifmetik

print(conn.execute(addresses_avg_id).fetchone())