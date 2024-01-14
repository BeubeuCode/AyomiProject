import sqlite3
import threading

class Database:
    def __init__(self, db_name):
        print('Database.__init__')
        self.db_name = db_name
        self.connection = None
        self.local_context = threading.local()
        self.connect()
        self.create_results_table()


    def get_conn(self):
        if not hasattr(self.local_context, "conn"):
            self.local_context.conn = sqlite3.connect(self.db_name)
        return self.local_context.conn

    def connect(self):
        print('Database.connect')
        self.get_conn()
 
    def disconnect(self):
        if hasattr(self.local_context, "conn"):
            self.local_context.conn.close()
            del self.local_context.conn


    def execute_query(self, query):
        print('Database.execute_query')
        cursor = self.get_conn().cursor()
        cursor.execute(query)
        self.get_conn().commit()
        return cursor.fetchall()

    def create_results_table(self):
        print('Database.create_results_table')
        query = '''
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            calculation_query TEXT,
            result REAL
        )
        '''
        self.execute_query(query)

    def get_all_results(self):
        query = '''
        SELECT * FROM results
        '''
        return self.execute_query(query)

    def insert_result(self, calculation_query, result):
        query = f'''
        INSERT INTO results (calculation_query, result)
        VALUES ('{calculation_query}', {result})
        '''
        self.execute_query(query)

    

    
