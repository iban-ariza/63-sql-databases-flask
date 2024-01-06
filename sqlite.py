import sqlite3

# connects to a database, otherwise it creates it
db = sqlite3.connect("books_collection.db")

# creates a cursor to interact with our database
cursor = db.cursor()

# tells the cursor to execute a function (can only be run ONCE)
# cursor.execute("CREATE TABLE books "
#                "(id INTEGER PRIMARY KEY, title varchar(250) "
#                "NOT NULL UNIQUE, author varchar(250) NOT NULL, "
#                "rating FLOAT NOT NULL)")

cursor.execute("INSERT INTO books "
               "VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# commit the command
db.commit()
db.close()




