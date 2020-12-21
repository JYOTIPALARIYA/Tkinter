import sqlite3

con=sqlite3.connect('mycompany.db') #need to create server to connect with database
cObj=con.cursor()#need to create an Object of cursor
cObj.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY,name TEXT,salary REAL,department TEXT,position TEXT)")
con.commit()

def insert(id,name,salary,department,position):
    cObj.execute("INSERT INTO student VALUES(?,?,?,?,?)",(id,name,salary,department,position))
    con.commit()
def update(dep,id):
    cObj.execute("Update student SET department=? where id=?",(dep,id))
    con.commit()

def sql_fetch():
    cObj.execute("SELECT * FROM student")
    result=cObj.fetchall()
    print(result)


def delete_all():
    cObj.execute("DELETE FROM student")
    con.commit()



insert(6,"Nancy",7000000000,"Python","Dev")
sql_fetch()
cObj.close()
con.close()
