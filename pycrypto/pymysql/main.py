import sqlite3

con = sqlite3.connect("mycompany.db")
cObj = con.cursor()

cObj.execute("CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY, name TEXT, salary REAL, department TEXT, pposition TEXT)")
con.commit()

def insert_value(id, name, salary, department, position):
    cObj.execute("INSERT INTO employees VALUES(?, ?, ?, ?, ?)",(id, name, salary, department, position))
    con.commit()

def update_value(dep, id):
    cObj.execute("UPDATE employees SET department=? WHERE id=?",(dep, id))
    con.commit()

def sql_fetch():
    cObj.execute("SELECT * FROM employees")
    result = cObj.fetchall()
        print(result)

def delete_all():
    cObj.execute("Delete from employees")
    con.commit()

    
cObj.close()
con.close()
