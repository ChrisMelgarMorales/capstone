from flask import Flask,request,jsonify
from flask_cors import CORS , cross_origin
import socket
import json
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/getstatus',methods = ['POST'])
@cross_origin(support_credentials=True)
def login():
        #testing edits on container based on local files
        #server only uses new app.py
        #when flask app is rerun when container restarts
        HOST = 'host.docker.internal'
        PORT = 5002
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(b'Hello World')
            data = s.recv(1024)
        f = open('data.json')
        data = json.load(f)
        json_str = json.dumps(data)
        return json_str, 200
'''try:
   if request.method == 'POST':
        try:
            channel = request.form.get('channel')
            mix = request.form.get('mix')
            command = request.form.get('command')
            PORT = request.form.get('PORT')
            HOST = request.form.get('HOST')
            prefix = 'get MIXER:Current/InCh/'
            LabelInfix= 'Label/Name'
            ToMixInfix =['ToMix/','On','Level','Pan']
            postfix = ' {} {}'.format(channel,mix)

            if command is '1111':

                import socket
                commandList = []
                str = prefix+LabelInfix+postfix
                commandList.append(str)
                for i in range(1,4):
                    tempstr=prefix+ToMixInfix[0]+ToMixInfix[i]+postfix
                    commandList.append(tempstr)
                
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((HOST, PORT))
                    for i in commandList:
                        s.sendall(i.encode('utf-8'))
                        data = s.recv(1024)
                        print(f"Received {data!r}")
        except Exception as e:

            result = {'a': str(e)}
            return result, 201
        '''