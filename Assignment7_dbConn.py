import psycopg2

def table():
    con=psycopg2.connect(dbname="postgres",user="postgres",password="mypassWord",host="localhost",port="5432")
    print("Connection Successful")

    cursor=con.cursor()
    cursor.execute('''create table employees(Name Text, ID int, age int);''')
    con.commit()
    print("Table successfully created.")
    con.close()
    print("Connection Closed")

def data():
    con=psycopg2.connect(dbname="postgres",user="postgres",password="mypassWord",host="localhost",port="5432")
    print("Connection Successful")
    cursor=con.cursor()    
    name=input("Enter Employee Name:")
    id=input("Enter Employee ID:")
    age=input("Enter Employee's age:")
    query='''insert into employees(Name,ID,age) values(%s,%s,%s);'''
    cursor.execute(query,(name,id,age))
    con.commit()
    print("Data successfully added.")
    con.close()
    print("Connection Closed")

def extract():
    con=psycopg2.connect(dbname="postgres",user="postgres",password="mypassWord",host="localhost",port="5432")
    print("Connection Successful")
    cursor=con.cursor()    
    cursor.execute('''select * from employees;''')
    con.commit()
    data=cursor.fetchone()
    print(data[0])
    con.close()
    print("Connection Closed")

#table()
#data()
extract()