# from msilib.schema import Error
import pymysql

# try:
connection = pymysql.connect(host="localhost", port=88, user="aris", passwd="1114", database="bloggle")

mySql_Create_Table_Query = """CREATE TABLE Laptop ( 
                            Id int(11) NOT NULL,
                            Name varchar(250) NOT NULL,
                            Price float NOT NULL,
                            Purchase_date Date NOT NULL,
                            PRIMARY KEY (Id)) """

# cursor = connection.cursor()
# result = cursor.execute(mySql_Create_Table_Query)
# print("Laptop Table created successfully ")

connection.close()

# except error:
#     print("Failed to create table in MySQL: {}".format(error))
# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")

