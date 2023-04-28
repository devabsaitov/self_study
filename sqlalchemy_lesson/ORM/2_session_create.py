from sqlalchemy import create_engine, Column, Integer, String, func
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('postgresql://postgres:1@localhost/news_db')

Base = declarative_base()
class Customers(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)


Session = sessionmaker(bind=engine)
session = Session()

customers1 = Customers(name = 'Abduqodir' , address = 'Toshkent' , email = 'John@gmail.com')
customers2 = Customers(name = 'John' , address = 'Toshkent1' , email = 'Hoshim@gmail.com')
customers3 = Customers(name = 'Hoshim' , address = 'Toshkent2' , email = 'Polat@gmail.com')
customers4 = Customers(name = 'Polat' , address = 'Toshkent3' , email = 'Sarvar@gmail.com')
customers5 = Customers(name = 'Sarvar' , address = 'Toshkent4' , email = '@gmail.com')

# ==================================== delete =================================
# session.query(Customers).filter(Customers.id == 1).delete(synchronize_session = False)

# # ==================================== add_all =================================
# session.add_all([customers1 , customers2, customers3, customers4 , customers5])

# ==================================== update =================================
# session.query(Clients).filter(Clients.id == client_id_list).update({'status': status})
# session.query(Customers).filter(Customers.id == 2).update({'name' : 'test'})


# ============================ all get data =================================================
# x = session.query(Customers).get(ident=4)
# x = session.query(Customers).filter(Customers.id == 2).all()


# ============================ group by =======================================
x = session.query(Customers.name , func.count(Customers.name)).group_by(Customers.name).all()































