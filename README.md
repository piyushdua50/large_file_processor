# Large file processor 
Aim is to build a system which is able to handle long running processes in a distributed fashion. 

### Problem statement 
We need to be able to import products from a CSV file and into a database. There are half a million product details to be imported into the database.

**Points to achieve**
1. Your code should follow concept of OOPS
2. Support for regular non-blocking parallel ingestion of the given file into a table. Consider thinking about the scale of what should happen if the file is to be processed in 2 mins.
3. Support for updating existing products in the table based on `sku` as the primary key. (Yes, we know about the kind of data in the file. You need to find a workaround for it)
4. All product details are to be ingested into a single table
5. An aggregated table on above rows with `name` and `no. of products` as the columns


**Language used- ** Python3
**Database used- ** MySQL

### Steps to run
1. Download the project using- 
2. Setup the database
  * Login to your MySQL database
  * Go to the src/database folder
  * Execute the SCHEMA.sql script in order to create and use the schema
  * Execute the PRODUCTS.sql in order the create the PRODUCTS table
  * Execute the PRODUCT_COUNT_DTL.sql in order to create the PRODUCT_COUNT_DTL table
3. Now install the python dependencies
  * pandas- `pip install pandas`
  * os- `pip install os`
  * mysql-connector- `pip install mysql-connector`
  * python-dotenv- `pip install python-dotenv`
4. Now place the database username, database passowrd and database name in .env file.
5. Execute this command- `python src/server.py`


