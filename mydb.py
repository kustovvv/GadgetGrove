import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'ddbs3421',
)

cursorObject = dataBase.cursor()
cursorObject.execute('CREATE DATABASE gadgetgrove')
print('All Done!')

