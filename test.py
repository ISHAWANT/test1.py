import mysql.connector as connection

mydb=connection.connect(host='localhost',database = 'rajabeta',user='root',passwd='mysql')

cursor=mydb.cursor()

# cursor.execute('create database bulb5')
# print('database created sucssefull')

# cursor.execute('show databases')

#print(cursor.fetchall())
# cursor.execute('use database bulb')
s="create table Details(cpn_name varchar(20), cpn_emp int(30),cpn_location varchar(25))"
cursor.execute(s)

#
p="insert into Details values('bosch' ,1000,'lonavala')"

cursor.execute(p)

mydb.commit()