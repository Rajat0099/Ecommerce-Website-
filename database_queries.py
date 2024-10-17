from database_setup import create_connection

def get_top_customers():
    conn = create_connection()
    cursor = conn.cursor()

    query = '''
        SELECT TOP 5 c.customer_id, c.name, SUM(od.quantity) AS total_books
        FROM Customers c
        JOIN Orders o ON c.customer_id = o.customer_id
        JOIN OrderDetails od ON o.order_id = od.order_id
        WHERE o.order_date >= DATEADD(YEAR, -1, GETDATE())
        GROUP BY c.customer_id, c.name
        ORDER BY total_books DESC;
    '''

    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()

# Call the function to display top customers
if __name__ == "__main__":
    get_top_customers()
