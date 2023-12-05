from flask import Flask, render_template, request, url_for, render_template, request, session
import sqlite3
#need below for bar chart of customer gender
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd
from datetime import date

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')

#Homepage
@app.route('/homepage')
def home():
    return render_template('homepage.html')


@app.route('/customers', methods=['GET', 'POST'])
def customers():

    if request.method == 'POST':


        return render_template ('customers.html')

    else: 
        return render_template('customers.html')
    
@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():

    if request.method == 'POST':


        return render_template ('add_customer.html')

    else: 
        return render_template('add_customer.html')
    

@app.route('/form_add_customer', methods=['GET', 'POST'])
def form_add_customer():

    submit = 0

    if request.method == 'POST':
        # Getting form data
        db_file = ('/Users/morgangutzwiller/Desktop/db_course/research_assign/retail_app.db')
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        first_name = request.form['fName']
        last_name = request.form['lName']
        gender = request.form['gender']
        DOB = request.form['DOB']

        cursor.execute("""
            SELECT MAX(customer_id) FROM customer; 
        """)
        new_id = cursor.fetchall()[0]
        new_id = new_id[0] + 1

        cursor.execute(
                f"""
                INSERT INTO customer (customer_id, customer_first_name, customer_last_name, 
                customer_gender, customer_dob) VALUES (?, ?, ?, ?, ?);""",
                (new_id, first_name, last_name, gender, DOB),
            )

        conn.commit()

        cursor.close()
        conn.close()

        submit = 1

    return render_template('form_add_customer.html', submit = submit)
    

@app.route('/products', methods=['GET', 'POST'])
def products():

    if request.method == 'POST':


        return render_template ('products.html')

    else: 
        return render_template('products.html')
    
@app.route('/get_product', methods=['GET', 'POST'])
def get_product():

    if request.method == 'POST':


        return render_template ('get_product.html')

    else: 
        return render_template('get_product.html')
    

@app.route('/form_get_product', methods=['GET', 'POST'])
def form_get_product():

    if request.method == 'POST':
        # Getting form data
        db_file = ('/Users/morgangutzwiller/Desktop/db_course/research_assign/retail_app.db')
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        product_id = request.form['product_id']

        cursor.execute("""
            SELECT 
                p.product_name,
                p.product_description,
                p.product_price,
                p.product_inventory,
                p.product_vendor
            FROM 
                product p
            WHERE 
                product_id = ?;
        """, (product_id,))

        product_info = cursor.fetchall()

        print("Product Information:", product_info)
        
        conn.close()

        return render_template('form_get_product.html', product_info = product_info)
    return render_template('form_get_product.html')



if __name__ == '__main__':
    app.run(debug=True)