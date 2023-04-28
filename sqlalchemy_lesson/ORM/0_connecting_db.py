from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:1@localhost/news_db") # postgresql://user:password@host/dbname

engine.connect()


# pip install SQLAlchemy
# pip install psycopg2-binary
#