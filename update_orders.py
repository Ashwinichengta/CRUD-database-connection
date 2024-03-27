# Update table using mysql.connector --Python

import mysql.connector as sql
import pandas as pd

db_connection=sql.connect(host='localhost',database='empdb',user='root',password='')
db_cursor=db_connection.cursor()
db_cursor.execute("update orders set ord_date='02/12/2023' where ccode='C005'")
db_connection.commit()
print(db_cursor.rowcount,"Data updated successfully!")

ch=pd.read_sql("select * from orders",con=db_connection)
print(ch)
