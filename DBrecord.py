import pymysql

conn = pymysql.connect(host='localhost', user='username', password='pwd', db='dbname', charset='utf8')

curs = conn.cursor()
sql = """insert into Data(CLK,TMP,CDS,BAT) values (%s, %s, %s, %s)"""

lst=list()
for idx in range(0,10):
	tmp=raw_input()
	lst.insert(idx,tmp)
	if idx == 3:
		print("list is full")
		break

curs.execute(sql, (lst[0],lst[1],lst[2],lst[3]))
conn.commit()
conn.close()

print(lst)
