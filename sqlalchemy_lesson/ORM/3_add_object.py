from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('postgresql://postgres:1@localhost/news_db')

Base = declarative_base()


class Customers(Base):
    __tablename__ = 'customers' # noqa

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)


class Sales(Base):
    __tablename__ = 'sales' # noqa

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String)
    email = Column(String, nullable=True)


# add object
Session = sessionmaker(bind=engine)
session = Session()

C1 = Customers(name='Dilshod', address='Sirdaryo', email='test@gmail.com')

session.add(C1)
session.add_all([
    Customers(name='Komal Pande', address='Koti, Hyderabad', email='komal@gmail.com'), # noqa
    Customers(name='Rajender Nath', address='Sector 40, Gurgaon', email='nath@gmail.com'),
    Customers(name='S.M.Krishna', address='Budhwar Peth, Pune', email='smk@gmail.com')])
session.commit()

Base.metadata.create_all(engine)
