'''
Create a table and modify
'''



import pymysql as sql

connection = sql.connect(host='localhost', user='root', password='pass')
cursor = connection.cursor()

cursor.execute("DROP DATABASE DB;")
cursor.execute("CREATE DATABASE DB;")
cursor.execute("USE DB;")
cursor.execute("CREATE TABLE Marks ("
               "Roll INT PRIMARY KEY,"
               "Name CHAR(10) NOT NULL,"
               "Marks INT NOT NULL"
               ");")
cursor.execute("INSERT INTO Marks (Roll, Name, Marks) VALUES"
               "(1, 'Anish', 40),"
               "(2, 'Neel', 60),"
               "(3, 'Arpita', 80);"
               )
cursor.execute("UPDATE Marks"
               " SET Marks = Marks + 20"
               " WHERE Name LIKE 'A%';")
cursor.execute("ALTER TABLE Marks"
               " RENAME COLUMN Name"
               " TO Student_Name;")
cursor.execute("ALTER TABLE Marks"
               " DROP PRIMARY KEY;")
cursor.execute("INSERT INTO Marks (Roll, Student_Name, Marks) VALUES"
               "(4, 'Abhay', 20);")
cursor.execute("DELETE FROM Marks"
               " WHERE Marks < 50;")

print("OUTPUT ----------------")
cursor.execute("SELECT * FROM Marks")
data = cursor.fetchall()
for line in data:
    print(line)
cursor.close()
connection.close()
