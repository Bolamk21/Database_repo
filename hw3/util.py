import psycopg2
from psycopg2 import Error

def connect_to_db(username='raywu1990',password='test',host='127.0.0.1',port='5432',database='dvdrental'):
	try:
		connection = psycopg2.connect(user=username, password=password, host=host, port=port, database=database)
		cursor = connection.cursor()
		print("connected to the database")
		return cursor, connection
	except (Exception, Error) as error:
		print("Error while connecting to PostgreSQL", error)
	

def disconnect_from_db(connection,cursor):
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed.")
    else:
    	print("Connection does not work.")

def run_and_fetch_sql(cursor):
	try:
		select_statement = """ SELECT * from basket_a;"""
		cursor.execute(select_statement)
		record = cursor.fetchall()
		return record
	except (Exception, Error) as error:
		print("Errors while executes the code: ", error)
	
def insert_into_basket_a(cursor, connection):
	try:
		ins_statement = """ INSERT INTO basket_a ("a", "fruit_a") VALUES ('5', 'Cherry')"""
		cursor.execute(ins_statement)
		connection.commit()
		return "Success!"
	except (Exception, Error) as error:
		print("Errors while executes the code: ", error)

def show_unique(cursor):
	try:
		unique_statement = """ SELECT * 
							FROM basket_a 
							full outer join basket_b on fruit_a = fruit_b 
							where fruit_a is NULL or fruit_b is NULL """
		cursor.execute(unique_statement)
		lst = cursor.fetchall()
		return lst
	except (Exception, Error) as error:
		print("Errors while executes the code: ", error)

