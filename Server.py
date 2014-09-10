from socket import *
from time import ctime
from Views import index

def Server(host='127.0.0.1', port=8090, bufferSize = 500, maxConnections = 500):
    '''Simple webserver to process all incoming requests'''
    addr = (host, port)
    con = socket()
    con.bind(addr)
    con.listen(maxConnections)
    print "Server started on: ", ctime()
    try:
        while True:
            client, clientAddr = con.accept()
            data = client.recv(bufferSize)
            print "Connnection accepted from: ", clientAddr[0]
            if not data:
                client.close()
            rem = data.splitlines()
            if len(rem) == 0:
                client.close()
            url = rem[0].split(' ')
            uri = url[1]
            
            if uri.startswith('/post'):
                client.send("Blog post Page")
                
            elif uri.startswith('/login'):
                client.send("Login page")
                
            elif uri.startswith('/signup'):
                client.send("Signup page")
                
            elif uri.startswith('/single'):
                client.send("Blog content page")
                
            elif uri.startswith('/static'):
                client.send("Static contents")
                
            elif uri == '/':
                client.send(index.header)
                
            client.close()
    except KeyboardInterrupt:
        print "Server shutdown"
        con.close()

if __name__ == '__main__':
    Server()
