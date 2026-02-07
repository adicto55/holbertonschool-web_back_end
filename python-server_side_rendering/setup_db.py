"""
Database setup script for creating and populating the SQLite database.
Run this script to create or reset the products database.
"""

import sqlite3

def create_database():
    """Create and populate the SQLite database with sample products."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # Drop existing table if it exists (for reset)
    cursor.execute('DROP TABLE IF EXISTS Products')
    
    # Create the Products table
    cursor.execute('''
        CREATE TABLE Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Insert sample data
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99),
        (3, 'Desk Chair', 'Furniture', 249.99),
        (4, 'Wireless Mouse', 'Electronics', 29.99),
        (5, 'Notebook', 'Stationery', 5.99)
    ''')
    
    conn.commit()
    conn.close()
    print("Database created successfully with 5 sample products!")

if __name__ == '__main__':
    create_database()
