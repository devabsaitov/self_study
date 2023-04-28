from sqlalchemy import create_engine
# pip install sqlalchemy
# pip install psycopg2-binary
# create  database news_db

engine = create_engine('postgresql://postgres:1@localhost/news_db', echo = True)

engine.connect()
