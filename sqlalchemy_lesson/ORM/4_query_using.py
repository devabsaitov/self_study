from pip._internal.utils.misc import protect_pip_from_modification_on_windows
from sqlalchemy import create_engine, Column, Integer, String, distinct, func
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('postgresql://postgres:1@localhost/news_db')

Base = declarative_base()

class Customers(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)

class Sales(Base):
    __tablename__ = 'sales'

    id = Column(Integer , primary_key=True)
    name = Column(String , nullable=False)
    address = Column(String)
    email = Column(String , nullable=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)

session = Session()

# ============================ column qo'shadi ===========================================
# a = session.query(Customers).add_columns(Customers.name).all()
# for i in a:
#     print(i)

# ========================================================================================

# ================================ data count ============================================

# a = session.query(Sales).count()
# print(a)

# ========================================================================================

# ================================ unique data -> distinct  ============================================
# a = session.query(Customers).with_entities(distinct(Customers.name)).all()
# for i in a:
#     print(i)
# ========================================================================================

# ================================ data delete  ============================================
# session.query(Sales).filter(Sales.name == 'Botirjon').delete(synchronize_session = False)
# session.commit()

# ========================================================================================

# ================================ like name   ============================================
# a = session.query(Customers).filter(Customers.name.like('D%')).all()
#
# for i in a:
#     print(i.name)

# ========================================================================================

# ================================ like name   ============================================
# a = session.query(Customers).with_entities(Customers.name , func.count(Customers.id)).group_by(Customers.name).all()
#
# for i in a:
#     print(i)

# ========================================================================================



