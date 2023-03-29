import socket
import os
server = socket.socket()
server.bind(("0.0.0.0", 8080))
server.listen()
html="""HTTP/1.1 200 OK
Content-type: text/html

<h1 style="color:red">Welcome to Podman Powered Web Page</h1>
"""
while True:
    client, addr = server.accept()
    req  = client.recv(1024)
    try:
        dir_list = "<br>".join(os.listdir("/data/"))
    except Exception as error:
        dir_list = f"<br>Error: {error}"
    resp = (html + dir_list).encode()
    client.send(resp)
    client.close()
server.close()
