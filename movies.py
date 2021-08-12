import sqlite3

conn = sqlite3.connect('test.db')
#print("HI!")

#command = "insert into movies (name ,actor, actress , release ) values('MISSION M','AKSHAY K','VIDYA B','2019')"

command = "select * from movies"
result = conn.execute(command)
for row in result:
    name,actor,actress,release =  row
    #print(name)
    #print(actor)
    #print(actress)
    #print(release)

    print(name,actor,actress,release)
