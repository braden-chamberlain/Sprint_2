# step 0 - import sqlite3
import sqlite3
import queries as q

# step 1 - connect to the database
# triple check the spelling of your database filename
connection = sqlite3.connect('rpg_db.sqlite3')

# step 2 - make the 'cursor'
# the cursor acts like a bank teller, so you don't mess with the vault even though your money's in there
cursor = connection.cursor()

# step 3 - write a query
'''see queries.py'''

# step 4 - execute the query on the cursor and fetch the results
# 'pulling the results' from the cursor
results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__ == '__main__':
    print(results[:5])