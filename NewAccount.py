import mysql.connector 
con = mysql.connector.connect(host='LocalHost',user='root',password='dps123',database='insta')
cur = con.cursor()

cur.execute("create table account(acc_name varchar(20),username varchar(20),password varchar(20))")

if con.is_connected():
    print("Connected")

ch = 'y'
while ch=='y' or ch=='Y':
    n = input('Do You Want To Make A New Account? :')

    if n=='yes' or n=='Yes':
        a = input("Enter Account Name:")
        b = input("Enter User Name:")
        c = input("Enter Password")
        d = input("Confirm Password:")
        if c == d:
            print("Account Created")
        else:
            print("Please retry")
        sql = "insert into account(acc_name,username,password) values(%s,%s,%s)"
        val = (a,b,c)
        cur.execute(sql,val)
        con.commit()
