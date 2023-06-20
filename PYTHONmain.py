import mysql.connector as sq
con=sq.connect(host="localhost",user="root",passwd="dps@123",database="sehdev")
if con.is_connected():
	print("Conneted to SQL")

