import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="demodb")
try:
    mycusor=mydb.cursor()
    # mycusor.execute("""INSERT INTO DEMO(
    # tc_id, username, password)
    # VALUES ('tc_002', 'Gagan', '1234')""")
    mycusor.execute("UPDATE demo SET `tc_id` = 'tc_003' WHERE (`id` = '3'); ")
    mycusor.execute("delete from demo where id = 4;")
    mydb.commit()
    mycusor.execute("select * from demo")
    result=mycusor.fetchall()
    for i in result:
        print(i)
except Exception as ex:
    print (ex)