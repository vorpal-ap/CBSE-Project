'''
Add details of workers
'''


import pymysql as sql

connection = sql.connect(host='localhost', user='root', password='pass')
cursor = connection.cursor()

def printSQL():
    for line in cursor.fetchall():
        print(line)
    print()


cursor.execute("DROP DATABASE DB;")
cursor.execute("CREATE DATABASE DB;")
cursor.execute("USE DB;")
cursor.execute("CREATE TABLE WORKER ("
               "ECODE INT PRIMARY KEY,"
               "NAME CHAR(50),"
               "DESIG CHAR(50),"
               "PLEVEL CHAR(4),"
               "DOJ DATE,"
               "DOB DATE"
               ");")
cursor.execute("INSERT INTO WORKER VALUES"
               "(11, 'Radhe Shyam', 'Supervisor', 'P001', '2004-09-13', '1981-08-23'),"
               "(12, 'Chander Nath', 'Operator', 'P003', '2010-02-22', '1987-07-12'),"
               "(13, 'Fizza', 'Operator', 'P003', '2009-06-14', '1983-10-14'),"
               "(15, 'Ameen Ahmed', 'Mechanic', 'P002', '2006-08-21', '1984-03-13'),"
               "(18, 'Sanya', 'Clerk', 'P002', '2005-12-19', '1983-06-09');")

cursor.execute("SELECT * FROM WORKER ORDER BY DOB DESC;")
printSQL()
cursor.execute("SELECT NAME, DESIG FROM WORKER WHERE PLEVEL = 'P001' or PLEVEL = 'P002';")
printSQL()
cursor.execute("SELECT * FROM WORKER WHERE DOB BETWEEN '1984-01-19' AND '1987-01-18';")
printSQL()
cursor.execute("INSERT INTO WORKER VALUES (19, 'Daya Kishor', 'Operator', 'P003', '2008-06-18', '1984-07-11');")
cursor.execute("SELECT * FROM WORKER")
printSQL()

cursor.close()
connection.close()
