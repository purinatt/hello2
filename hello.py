import socket
def mainRun():
    host = "127.0.0.1"
    port = 5000
    server=socket.socket()
    server.bind((host,port)) #ผูกobject
    server.listen(1) #กำหนดจำนวน client
    print("รอการเชื่อมต่อจาก Client :")
    client,addr=server.accept()
    print("Connect From :" + str(addr))
    #กระบวนการรับส่งข้อมูลระหว่างเครื่อง
    while True :
        #รับข้อมูล
        data = client.recv(1024).decode('utf-8')
        if not data :
            break
        print("Message from Client :"+data)
        #ส่งข้อมูลกลับไป
        data=str(data.upper())
        client.send(data.encode('utf-8'))
    client.close()
if __name__ == '__main__':
    mainRun()
