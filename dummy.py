import mysql.connector as connection

mydb=connection.connect(host='localhost',database = 'bulb1',user='root',passwd='mysql')

cursor=mydb.cursor()

#cursor.execute('create database bulb')

#cursor.execute('show databases')

#print(cursor.fetchall())
# cursor.execute('use database bulb')
v="create table test(cpn_name varchar(20) , cpn_emp int(25),cpn_location varchar(26))" #both line works
cursor.execute(v)
# cursor.execute("create table mango(cpn_name varchar(20) , cpn_emp int(25),cpn_location varchar(26))")


s="insert into test values('bosch' ,1000,'lonavala')"

cursor.execute(s)

mydb.commit()


