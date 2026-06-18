import sqlite3


con=sqlite3.connect("project.db")
cursor=con.cursor()

cursor.execute()  # add create table query

con.commit()
con.close()
import sqlite3

#COnnect with Database
con = sqlite3.connect("project.db")
cursor = con.cursor()

#Query to create table
create_table_query = '''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
'''

#Execute the query
cursor.execute(create_table_query)

print("Table 'students' successfully created!")

#Save Changesto database
con.commit()
#close connection
con.close()




