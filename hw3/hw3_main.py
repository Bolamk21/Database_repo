from flask import Flask, render_template
import util

app = Flask(__name__)

username='raywu1990'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'

@app.route('/')
def index():
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    record = util.run_and_fetch_sql(cursor)
    if record == -1:
        print('Something is wrong with the SQL command')
    else:
        col_names = [desc[0] for desc in cursor.description]
        log = record[:5]
    util.disconnect_from_db(connection,cursor)
    return render_template('index.html', sql_table = log, table_title=col_names)

@app.route('/api/update_basket_a')
def update_basket_a():
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    msg = util.insert_into_basket_a(cursor, connection)
    util.disconnect_from_db(connection,cursor)
    return msg

@app.route('/api/unique')
def show_unique():
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    tbl = util.show_unique(cursor)
    col_names = ['a', 'fruit_a', 'b', 'fruit_b']
    util.disconnect_from_db(connection,cursor)
    return render_template('index.html', sql_table = tbl, table_title=col_names)

if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)