# Large file processor 
Aim is to build a system which is able to handle long running processes in a distributed fashion. It imports products from a CSV file and load it into a database. There are half a million product details to be imported into the database.


**Technology-** Python and MySQL


### Steps to run
1. Download the project using- `https://github.com/piyushdua50/large_file_processor.git`
2. Place the `products.csv` file in src folder.
3. Setup the database.
   * Login to your MySQL database
   * Go to the src/database folder
   * Execute the `SCHEMA.sql` script in order to create and use the schema
   * Execute the `PRODUCTS.sql` in order the create the PRODUCTS table
   * Execute the `PRODUCT_COUNT_DTL.sql` in order to create the PRODUCT_COUNT_DTL table
4. Now install the python dependencies
   * pandas- `pip install pandas`
   * os-sys- `pip install os-sys`
   * mysql-connector- `pip install mysql-connector`
   * python-dotenv- `pip install python-dotenv`
5. Now provide the database user, database password and database name in .env file.
6. Execute this command- `python src/server.py`

