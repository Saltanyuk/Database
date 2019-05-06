Import psycopg2


class Database:
    def __init__(self, host='your_host', dbuser='your_user', password='your_password', DB='yourDB'):
        self.host = host
        self.dbuser = dbuser
        self.password = password
        self.DB = DB

    def connection(self, sql, data):
        box = []
        conn = psycopg2.connect(host=self.host, user=self.dbuser, password=self.password, dbname=self.DB)
        cursor = conn.cursor()
        cursor.execute(sql, data)
        rows = cursor.fetchall()
        conn.close()
        for i in rows:
            try:
                box.append(''.join(i))
            except Exception:
                continue
        return box

    def insertion(self, sql, data):
        conn = psycopg2.connect(host=self.host, user=self.dbuser, password=self.password, dbname=self.DB)
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        conn.close()
