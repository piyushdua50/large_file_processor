# importing the libraries
import os
from dotenv import load_dotenv
from mysql.connector import (connection)


class DatabaseHelper:
    def __init__(self):
        load_dotenv()
        self.schema = os.getenv('SCHEMA_NAME')
        try:
            self.db = connection.MySQLConnection(
                host='localhost',
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                charset='utf8',
                database=os.getenv('DB_NAME'))

            # Get the cursor, which is used to traverse the database
            self.cursor = self.db.cursor()

        except:
            print("Error in connecting to the Database...............")

    def load_data(self, data):
        # Query to insert csv data into the table
        add_product = 'INSERT INTO {}.PRODUCTS (NAME, SKU, DESCRIPTION) VALUES (%s, %s, %s)'.format(self.schema)

        # Insert DataFrame to Table
        for row in data.itertuples():
            self.cursor.execute(add_product, (row.name, row.sku, row.description))
            if (row.Index + 1) % 5000 == 0:
                self.db.commit()  # commit the database transaction after every 5000 records

        self.db.commit()
        return self.cursor.rowcount

    def get_products(self):
        # Returns the number of records inserted into the table
        query = 'SELECT COUNT(*) FROM {}.PRODUCTS'.format(self.schema)
        self.cursor.execute(query)
        no_of_records = self.cursor.fetchall()[0][0]
        return no_of_records

    def get_products_count(self):
        # Returns the number of products with their respective count
        query = '''INSERT INTO {}.PRODUCT_COUNT_DTL
                SELECT NAME PRODUCT_NAME, COUNT(NAME) NO_OF_PRODUCTS FROM {}.PRODUCTS 
                GROUP BY NAME ORDER BY COUNT(NAME) DESC'''.format(self.schema, self.schema)
        self.cursor.execute(query)

        self.db.commit()      # commit the database transaction after DML statement
        return self.cursor.rowcount

    def update_product(self, p_sku, p_name, p_desc):
        # Returns the number of products updated with provided product_sku
        query = '''UPDATE {}.PRODUCTS SET NAME = %s, DESCRIPTION = %s WHERE SKU=%s'''.format(self.schema)
        data = (p_name, p_desc, p_sku)
        self.cursor.execute(query, data)

        self.db.commit()      # commit the database transaction after DML statement
        return self.cursor.rowcount

    def close_connection(self):
        # Close the database connection
        self.db.close()
