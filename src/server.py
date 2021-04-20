# importing the libraries
import pandas as pd
from src.helpers import DatabaseHelper

# Import the CSV file
data = pd.read_csv('products.csv')
df = pd.DataFrame(data, columns=['name', 'sku', 'description'])

# connect to the database
helpers = DatabaseHelper()

# load the csv file into database table
helpers.load_data(df)
print("All data loaded successfully.............")

# Get the number of records inserted into the table
records = helpers.get_products()
print("Number of records inserted are: ", records)

# Get the number of products
products = helpers.get_products_count()
print("Number of products are: ", products)

# Update the product with given product sku
sku = 'do-many-avoid'
updated_products = helpers.update_product(sku, 'Tiffany_Johnson_updated_product_name', 'Born_tree_wind_updated_product_description')
print("Number of updated products with sku [", sku, "] are: ", updated_products, sep='')

# load the csv file twice into database table in order to check the update product
helpers.load_data(df)

# Printing the respective counts
print("Number of records in products table is: ", helpers.get_products())
print("Number of records in products_count_dtl table is: ", products)

# close the database connection
helpers.close_connection()