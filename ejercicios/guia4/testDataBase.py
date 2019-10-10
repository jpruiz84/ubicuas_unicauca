import sqlite3
conn = sqlite3.connect('example.db3')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE students (fecha text, nombre text, apellido text, edad integer)''')

# Insert a row of data
c.execute("INSERT INTO students VALUES ('2017-09-04','Juan','Ruiz',30)")

# Save (commit) the changes
conn.commit()

# Close connection
conn.close()