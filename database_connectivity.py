import sqlite3




######## Creating a Sample Table ########




# establishing a database connection
con = sqlite3.connect('TEST.db')

# preparing a cursor object
cursor = con.cursor()

# preparing sql statements
sql1 = 'DROP TABLE IF EXISTS EMPLOYEE'
sql2 = '''
       CREATE TABLE EMPLOYEE (
       EMPID INT(6) NOT NULL,
       NAME CHAR(20) NOT NULL,
       AGE INT,
       SEX CHAR(1),
       INCOME FLOAT
       )
      '''
      
# executing sql statements
cursor.execute(sql1)
cursor.execute(sql2)

# closing the connection
con.close()




######## Inserting a Sample Data ########




# establishing the connection
con = sqlite3.connect('TEST.db')

# preparing a cursor object
cursor = con.cursor()

# preparing sql statement
rec = (456789, 'Frodo', 45, 'M', 100000.00)
sql = '''
      INSERT INTO EMPLOYEE VALUES ( ?, ?, ?, ?, ?)
      '''
      
# executing sql statement using try ... except blocks
try:
    cursor.execute(sql, rec)
    con.commit()
except Exception as e:
    print("Error Message :", str(e))
    con.rollback()

# closing the database connection
con.close()


con = sqlite3.connect('TEST.db')
cursor = con.cursor()

# preparing sql statement
records = [
    (123456, 'John', 25, 'M', 50000.00),
    (234651, 'Juli', 35, 'F', 75000.00),
    (345121, 'Fred', 48, 'M', 125000.00),
    (562412, 'Rosy', 28, 'F', 52000.00)
    ]
sql = '''
       INSERT INTO EMPLOYEE VALUES ( ?, ?, ?, ?, ?)
      '''
      
# executing sql statement using try ... except blocks
try:
    cursor.executemany(sql, records)
    con.commit()
except Exception as e:
    print("Error Message :", str(e))
    con.rollback()

# closing the database connection
con.close()




######## Fetching Sample Data ########




# establishing the connection
con = sqlite3.connect('TEST.db')

# preparing a cursor object
cursor = con.cursor()

# preparing sql statement
sql = '''
       SELECT * FROM EMPLOYEE
      '''

# executing the sql statement using `try ... except`
try:
    cursor.execute(sql)
except:
    print('Unable to fetch data.')

# fetching the records
records = cursor.fetchall()

# Displaying the records
for record in records:
    print(record)

# closing the connection
con.close()




####################################################################



# Create Database
conn = sqlite3.connect('javatpoint.db')  
print("Opened database successfully");

 
# Create Table
conn = sqlite3.connect('javatpoint.db')  
print("Opened database successfully");    
conn.execute('''CREATE TABLE Employees 
       (ID INT PRIMARY KEY     NOT NULL, 
       NAME           TEXT    NOT NULL, 
       AGE            INT     NOT NULL, 
       ADDRESS        CHAR(50), 
       SALARY         REAL);''')  
print("Table created successfully");    
conn.close()


# Insert Records
conn = sqlite3.connect('javatpoint.db')  
print("Opened database successfully");  
conn.execute("INSERT INTO Employees (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Ajeet', 27, 'Delhi', 20000.00 )");  
conn.execute("INSERT INTO Employees (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 22, 'London', 25000.00 )");  
conn.execute("INSERT INTO Employees (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Mark', 29, 'CA', 200000.00 )");  
conn.execute("INSERT INTO Employees (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Kanchan', 22, 'Ghaziabad ', 65000.00 )");  
conn.commit()  
print("Records inserted successfully");  
conn.close()


# Select Records
conn = sqlite3.connect('javatpoint.db')  
data = conn.execute("select * from Employees");  
for row in data:  
   print("ID = ", row[0])  
   print("NAME = ", row[1])  
   print("ADDRESS = ", row[2])  
   print("SALARY = ", row[3])  
conn.close();

