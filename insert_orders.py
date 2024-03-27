# inserting data in a table by using python program

import mysql.connector as sql
import pandas as pd # Panal data

db_connection=sql.connect(host='localhost',database='empdb',user='root',password='')
db_cursor=db_connection.cursor()
db_cursor.execute("insert into orders(id,ord_date,icode,ccode)values(6,'12/8/2023','i006','C006')")
db_connection.commit()
print(db_cursor.rowcount,"Record Inserted.")

ch=pd.read_sql("select * from orders",con=db_connection)
print(ch)
