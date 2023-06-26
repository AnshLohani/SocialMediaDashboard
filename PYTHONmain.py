import mysql.connector as sq

#######################################################

con=sq.connect(user="root",passwd="2006")
if con.is_connected():
    print("Connected to MYSQL")
else:
    print("Error!")
cursor=con.cursor()
con.commit()

#created table in sql
#cursor.execute("create table instagram(Name varchar(25),Followers int,Average_Likes int,Posts int);")

########################################################


#used the SocialMedia Database that we already created
cursor.execute("use SocialMedia")


#function to add values to the table: Currently not working
def add_vals(name,followers,average_likes,posts):
    cursor.execute("insert into instagram values('{}',{},{},{});".format(name,followers,average_likes,posts))
    

add_vals(name='Abhinav',followers=1,average_likes=1,posts=1)

#########################################################

#function to describe the table and print it into python: Currently not working
def desc(base):
    x= cursor.execute("desc {}".format(base))
    return x

print(desc(base='instagram'))


########################################################
