import cx_Oracle

dsn_tns = cx_Oracle.makedsn('LAPTOP-AIT9NR87', '1521', service_name='XE') 
conn = cx_Oracle.connect(user='SYSTEM', password='toor', dsn=dsn_tns) 
cx = conn.cursor()
l=[]
cx.execute("delete from students")
file=open('namelist.txt','r')
for i in file:
	k=[]
	for j in i.split(';'):
		k.append(j)
	cx.prepare('insert into students values(:r,:n)')
	cx.execute(None,{'r':k[0],'n':k[1]})

conn.commit()
conn.close()
