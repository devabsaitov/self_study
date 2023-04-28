import psycopg2
from psycopg2.extras import DictCursor


class DB:
    def __init__(self, database, user, password, host, port, cursor_factory=None):
        self.conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port,cursor_factory=cursor_factory)
        self.cur = self.conn.cursor()

    def select(self, table_name, **kwargs):
        params = ",".join((["%s"]*len(kwargs)))
        query = "select * from %s  where {0}".format(params)
        print(query)



obj = DB("p11_db", "postgres", "1", "localhost", "5432", DictCursor)
print(obj.select("users", id=1, name = "Dilshod"))
