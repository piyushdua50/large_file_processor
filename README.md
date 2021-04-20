# Large file processor 
Aim is to build a system which is able to handle long running processes in a distributed fashion. We need to be able to import products from a CSV file and into a database. There are half a million product details to be imported into the database.


**Points to achieve**
1. Your code should follow concept of OOPS
2. Support for regular non-blocking parallel ingestion of the given file into a table. Consider thinking about the scale of what should happen if the file is to be processed in 2 mins
3. Support for updating existing products in the table based on `sku` as the primary key. (Yes, we know about the kind of data in the file. You need to find a workaround for it)
4. All product details are to be ingested into a single table
5. An aggregated table on above rows with `name` and `no. of products` as the columns


**Technology-** Python3 and MySQL


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
   * os-sys `pip install os-sys`
   * mysql-connector- `pip install mysql-connector`
   * python-dotenv- `pip install python-dotenv`
5. Now place the database username, database password and database name in .env file.
6. Execute this command- `python src/server.py`


### Points achieved
1. Your code should follow concept of OOPS. 
   * **Achieved**
2. Support for regular non-blocking parallel ingestion of the given file into a table. 
   * **Achieved**, Used an approach which will commit the ingestion of data after every 5000 records to provide regular non-blocking parallel ingestion of the given file into a table   
3. Support for updating existing products in the table based on sku as the primary key.
   * **Achieved**, Used an approach to update a product based on their `sku`    
4. All product details are to be ingested into a single table.
   * **Achieved**, all products details are ingested in `PRODUCTS` table. 
5. An aggregated table on above rows with name and no. of products as the columns.
   * **Achieved**, all product_name and their no_of_products are ingested in `PRODUCT_COUNT_DTL` table.

6. Number of entries in `PRODUCTS` table is- 1000000
7. Number of entries in `PRODUCT_COUNT_DTL` table is- 222024
8. 10 Sample Entries from `PRODUCTS` table-
   * Note- Only Name and SKU are shown here in sample entries due to large values of description
     
 +--------------------------------------+---------------------+
| NAME                                 | SKU                 |
+--------------------------------------+---------------------+
| Bryce Jones                          | lay-raise-best-end  |
| John Robinson                        | cup-return-guess    |
| Theresa Taylor                       | step-onto           |
| Roger Huerta                         | citizen-some-middle |
| John Buckley                         | term-important      |
| Tiffany_Johnson_updated_product_name | do-many-avoid       |
| Roy Golden DDS                       | help-return-art     |
| David Wright                         | listen-enough-check |
| Anthony Burch                        | anyone-executive    |
| Lauren Smith                         | grow-we-decide-job  |
+--------------------------------------+---------------------+

8. 10 Sample Entries from `PRODUCT_COUNT_DTL` table-

+-------------------+----------------+
| PRODUCT_NAME      | NO_OF_PRODUCTS |
+-------------------+----------------+
| Michael Smith     |            247 |
| Michael Johnson   |            187 |
| Robert Smith      |            167 |
| Christopher Smith |            159 |
| David Smith       |            158 |
| John Smith        |            157 |
| Michael Williams  |            157 |
| James Smith       |            152 |
| Jennifer Smith    |            151 |
| Michael Brown     |            148 |
+-------------------+----------------+


### Improvement required
* Can make a good UI based system which will take a CSV file as an input and process it into a required table.


