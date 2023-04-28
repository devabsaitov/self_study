from sqlalchemy import create_engine, Table, MetaData, column, Column, Integer, String, ForeignKey, select, text

engine = create_engine('postgresql://postgres:1@localhost/news_db', echo = True)

meta = MetaData()
students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('first_name', String),
    Column('last_name', String)
)

address = Table(
    'address' , meta ,
    Column('id' , Integer , primary_key=True),
    Column('name' , String),
    Column('email' , String),
    Column('st_id' , ForeignKey('students.id'))
)


meta.create_all(engine)

# conn = engine.connect()





















# query = students.insert().values([
#                                   {'name': 'Akmal', 'lastname': 'pardaboyev'},
#                                   {'name': 'Jamshid', 'lastname': 'nuriddinov'}]
#                                  )
# conn.execute(query)

# query = addresses.insert().values([{'st_id': 1, 'postal': 'Tashkent','email': 'test@2112.gmail.com'},{'st_id': 3, 'postal': 'Samarkand','email': 'test@9098.gmail.com'},{'st_id': 5, 'postal': 'Andijan','email': 'test@5467.gmail.com'}])
# conn.execute(query)

# join_table = select([students.c.name, addresses.c.postal]).where(students.c.id == addresses.c.st_id)
# result = conn.execute(students.select())
# for i in result:
#     print(i.name)


# insert into users(name, balance, passport_series, passport_number) values (select md5('hello'), floor(random()*(1000000-100+1)+100), ('{AA,AC,AB}'::text[])[ceil(random()*3)] , floor(random()*(9999999-1000000+1)+1000000) from generate_series(1, 9))


