import sqlite3
from _config import DATABASE_PATH
with sqlite3.connect(DATABASE_PATH) as connection:
	c=connection.cursor()

	c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL, status INTEGER NOT NULL)""")
     #DUMMY TASKS ADDED TO TEST THE FUNCTIONALITY
	c.execute('INSERT INTO tasks(name,due_date, priority,status)''VALUES("FINISH THIS","03/25/2017", 10,1)')

	c.execute('INSERT INTO tasks(name,due_date, priority,status)''VALUES("COMPLETE THIS","03/25/2017", 10,1)')


