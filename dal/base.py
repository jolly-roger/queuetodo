import psycopg2

from . import constants


class base(object):
    def __init__(self):
        conn = psycopg2.connect(constants.DB_CONNECTION)
        cur = conn.cursor()
    
    def close(self):
        self.cur.close()
        self.conn.close()