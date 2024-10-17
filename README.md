# E-Commerce System Project

## Overview
This project is a simple e-commerce system that manages users, products, orders, and payments using Python and Microsoft SQL Server.

## Project Files
```
ecommerce_project/
│
├── database_setup.py       # Sets up the database connection
├── ecommerce_system.py      # Contains classes for users, products, and orders
├── inventory_management.py   # Manages inventory and order processing
└── database_queries.py      # Runs queries to fetch data from the database
```

## Requirements
- Python 3.x
- Microsoft SQL Server
- `pyodbc` library for connecting Python to SQL Server

## Setup Instructions

1. **Install Python**: Download from [python.org](https://www.python.org/downloads/).
2. **Install VS Code**: Download from [code.visualstudio.com](https://code.visualstudio.com/).
3. **Install Required Packages**: Open the terminal in VS Code and run:
   ```bash
   pip install pyodbc
   ```

4. **Set Up the Database**:
   - Open SQL Server Management Studio (SSMS).
   - Create a new database called `BookstoreDB`.
   - Create the necessary tables using provided SQL scripts.

5. **Running the Project**:
   - Open the terminal and run:
     ```bash
     python database_setup.py
     python ecommerce_system.py
     python inventory_management.py
     python database_queries.py
     ```

## Output
- The output from `database_queries.py` will show the top 5 customers who purchased the most books.

