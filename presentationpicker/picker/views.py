from django.shortcuts import render , redirect
import cx_Oracle
import random
# Create your views here.


log=False
def home(request):
	if log==False:
		return redirect('login')
	else:
		if request.method=='POST':
			n=int(request.POST.get('num'))
			name=str
			names=[]
			dsn_tns = cx_Oracle.makedsn('LAPTOP-AIT9NR87', '1521', service_name='XE') 
			conn = cx_Oracle.connect(user='SYSTEM', password='toor', dsn=dsn_tns) 
			cx = conn.cursor()
			rolls=[]
			for i in range(n):
				cx.execute('select * from (select * from students order by DBMS_RANDOM.value) where rownum=1')
				r=str
				for o in cx:
					k=[]
					for j in o:
						k.append(j)
					r=k[0]
					name=k[1]
					break
				cx.prepare('delete from students where roll=:r')
				cx.execute(None,{'r':r})
				rolls.append([r,name])
			conn.commit()
			return render(request,'picker/index.html',{'roll':rolls})
		else:
			return render(request,'picker/index_number.html')

def login(request):
	global log
	if request.method=='POST':
		user,password=(request.POST.get('username'),request.POST.get('password'))
		if user=='kundan' and password=='8011f0a9':
			log=True
			return redirect('picker-home')
		else:
			return render(request,'picker/login.html')
				
	return render(request,'picker/login.html')