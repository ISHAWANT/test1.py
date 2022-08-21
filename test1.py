import mysql.connector as connection

try:
    # mydb = connection.connect(host="localhost", user="root", passwd="mysql",use_pure=True)
    # check if the connection is established
    # print(mydb.is_connected())
# step1
#     cursor = mydb.cursor()
    # query = "SHOW DATABASES"
    # cursor.execute(query)
# step2
#     query = "Create database bulb1;"
#     cursor.execute(query)



# step3
#     query = "SHOW DATABASES"
#     cursor.execute(query)
#     print(cursor.fetchall())
#     mydb.close()

# step4: +5 first create a database in workbench
    mydb = connection.connect(host="localhost", database = 'bulb1',user="root", passwd="mysql",use_pure=True)
    print(mydb.is_connected())
    cursor = mydb.cursor()
    # c= "CREATE TABLE bulbDetails(cpn_name varchar(20), cpn_emp int(30),cpn_location varchar(25))"
    # cursor.execute(c)
# STEP5:
    s = "insert into bulbDetails values('bosch' ,1000,'lonavala')"

    cursor.execute(s)
    print('values inseted')
    # r=select * from bulbDetails


    # print(cursor.fetchall())
    mydb.commit()

except Exception as e:
    print(str(e))
    print(str(e))