import psycopg2
from psycopg2.extras import DictCursor

conn = psycopg2.connect(database = "p11_db" ,
                        user = "postgres" ,
                        password = "1",
                        host = "localhost",
                        port = "5432",
                        cursor_factory=DictCursor
                        )

cur = conn.cursor()

cur.execute("select * from student;")
for i in cur.fetchall():
    print(i["name"])

