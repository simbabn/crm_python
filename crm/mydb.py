import mysql.connector 

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password"
)

# prepare cursor object

cursorObject = dataBase.cursor()

# create dabase 
cursorObject.execute("CREATE DATABASE crm_tuto")

#print
print('All done !')