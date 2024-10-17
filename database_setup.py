import pyodbc

def create_connection():
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=LAPTOP-6GARQN2O\\SQLEXPRESS;'
        'DATABASE=BookstoreDB;'
        'Trusted_Connection=yes;'
    )
    return conn
