import requests
import json
from os import path

# # exists = path.exists('/home/navgurukul014/Documents/output.json')

# # if exists:
# # 	file = open('/home/navgurukul014/Documents/output.json')
# # 	var = file.read()
# # 	print (var,"\n")
# # else:
srvr="http://saral.navgurukul.org/api/courses"
store=requests.get(srvr)
top=store.json()
with open("act.json","w") as count:
	json.dump(top,count)
 
with open("act.json","r") as count:
	var=json.load(count)
print(var,"\n")
# print (type(var))
a=0
for i in var['availableCourses']:
	a=a+1
	sew=(a,i["name"])
	print(sew)
user=int(input("entr the number\n"))
r=(var['availableCourses'])
var=str((r[user-1]["id"]))
# print (var)
new_url = 'http://saral.navgurukul.org/api/courses/'+str(var)+'/exercises'
print (new_url)
page=requests.get(new_url)
war=page.json()
# print(war)
b=war['data']
# print (b)
num=0 
for j in b:
	num+=1
	dr=(num,j['name'])
	print (dr)
user1=int(input("enter the number\n"))
f=(war['data'])
slug1 = f[user1-1]['slug']
print (slug1)
url1 = 'http://saral.navgurukul.org/api/courses/{}/exercise/getBySlug?slug={}'.format(var,slug1)
# print(url1)
page1=requests.get(url1)
war1=page1.json()
print (war1['content'])