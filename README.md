# Database_repo
Kameron G. Bolam
John Russell

This project allows a user to insert a new row into the specified table using a webpage url, and allows a user to view the unique items in basket_a and basket_b.

util.py contains the functionality code for these 2 specifications.
    The "insert_into_basket_a" function is used to insert a new row into the specified table
    The "show_unique" function is used to show the unique items in basket_a and basket_b
    The other functions such as "connect_to_db", "disconnect_from_db", and "run_and_fetch_sql" are used to connect to the database, fetch the results, and disconnect from the database when finished.

hw3_main.py contains the functionality code for the flask application that is responsible for creating and loading the webpage itself.
    The first app.route('/') activates the "index" function when the user loads that specific url. The index function connects to the database and displays the results from the "run_and_fetch_sql" function.
    The second app.route('/api/update_basket_a') activates the "update_basket_a" function when the user loads that specific url. The update_basket_a function connects to the database and inserts the specified row into that data table. The function then disconnects from the database and returns the message specified by the function, and that message is displayed on the webpage.
    The third app.route('/api/unique') activates the "show_unique" function when the user loads that specific url. The show_unique function connects to the database, and calls the show_unique function from util.py which returns the unique values in basket_a and basket_b. These values are then inserted into a table on the webpage. The function disconnects from the database before returning the webpage.

## Quick Start
First, we need to install a Python 3 virtual environment with:
```
sudo apt-get install python3-venv
```

Create a virtual environment:
```
python3 -m venv python_venv
```

You need to activate the virtual environment when you want to use it:
```
source python_venv/bin/activate
```

To fufil all the requirements for the python server, you need to run:
```
pip3 install -r requirements.txt
```
Because we are now inside a virtual environment. We do not need sudo.

Then you can start the server with:
```
python3 hw3_main.py