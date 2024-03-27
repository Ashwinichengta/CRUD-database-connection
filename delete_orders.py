# Deleting data from a table using python program

import mysql.connector as sql
import pandas as pd

db_connection=sql.connect(host='localhost',database='empdb',user='root',password='')
db_cursor=db_connection.cursor()
db_cursor.execute("delete from orders where id=6")
db_connection.commit()# stores data 100%
print(db_cursor.rowcount,"Record Deleted successfully")

ch=pd.read_sql("select * from orders",con=db_connection)
print(ch)
