import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def create_database():
    """Create and populate the SQLite database."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Check if table is empty before inserting
    cursor.execute('SELECT COUNT(*) FROM Products')
    if cursor.fetchone()[0] == 0:
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

# Initialize database when app starts
create_database()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    except FileNotFoundError:
        items_list = []
    except json.JSONDecodeError:
        items_list = []
    
    return render_template('items.html', items=items_list)

def read_json_products():
    """Read products from JSON file."""
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def read_csv_products():
    """Read products from CSV file."""
    products = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert price to float for consistency
                row['price'] = float(row['price'])
                row['id'] = int(row['id'])
                products.append(row)
    except FileNotFoundError:
        pass
    except (ValueError, KeyError):
        pass
    return products

def read_sql_products():
    """Read products from SQLite database."""
    products = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row  # Return rows as dictionaries
        cursor = conn.cursor()
        
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        
        for row in rows:
            products.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })
        
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    
    return products

@app.route('/products')
def products():
    """Display products from JSON, CSV, or SQL based on source parameter."""
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id', None)
    
    # Validate source parameter
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', 
                               error="Wrong source", 
                               products=None)
    
    # Read products based on source
    if source == 'json':
        products_list = read_json_products()
    elif source == 'csv':
        products_list = read_csv_products()
    else:  # source == 'sql'
        products_list = read_sql_products()
    
    # Filter by id if provided
    if product_id is not None:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products_list if p['id'] == product_id]
            
            if not filtered_products:
                return render_template('product_display.html', 
                                       error="Product not found", 
                                       products=None)
            
            return render_template('product_display.html', 
                                   error=None, 
                                   products=filtered_products)
        except ValueError:
            return render_template('product_display.html', 
                                   error="Invalid id parameter", 
                                   products=None)
    
    # Return all products if no id filter
    return render_template('product_display.html', 
                           error=None, 
                           products=products_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
