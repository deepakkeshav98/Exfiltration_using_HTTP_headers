from flask import Flask
from flask import request
import base64
app = Flask(__name__)
start=0
data=""

def hello():
    # return "Hello World!"
    filename=request.headers.get('filename')
    f=open(filename, "wb")
    global start
    global data
    d=request.headers.get('data')
    # print(d)
    if request.headers.get('start')=="true":
        start=1
        # print(start)
    
    
        # print(start)
    if request.headers.get('end')=="true":
        # print(data)
        # data=bytes(data)
        # print(data)
        data = base64.b64decode(data)
        # print(data)
        print("success")
        f.write(data)
        start=0

    if(start==0):
        data=""
        filename=""

    if(start==1):
        data=data+d
        # print(data)
        # print(d)

@app.route('/')

def declaration():
    start=0
    data=""
    hello()
    return ""


  
    
  
 



    # return "hello world"

if __name__ == '__main__':
    app.run()