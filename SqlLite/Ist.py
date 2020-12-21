import sqlite3

con=sqlite3.connect('mycompany.db') #need to create server to connect with database
cObj=con.cursor()#need to create an Object of cursor
# cObj.execute("CREATE TABLE student(id INTEGER PRIMARY KEY,name TEXT,salary REAL,department TEXT,position TEXT)")
# con.commit()

# cObj.execute("Insert into student VALUES(1,'Jyoti',7500,'Python','Development')")
# cObj.execute("Insert into student VALUES(?,?,?,?,?)",(2,'Harshit',50000,'JS','Developer'))
# cObj.execute("Update student SET department='Python' where id=2")
# cObj.execute("Update student SET department=? where id=?",('PHP',2))
cObj.execute("SELECT name,salary FROM student WHERE department='Python'")
# print(cObj.fetchall())
result=cObj.fetchall()
for i in result:
    # print(i)
    print(i[1])
cObj.execute("DELETE FROM student WHERE name=?",('Harshit',))
con.commit()#when we modify something we need to use commit
cObj.close()
con.close()
