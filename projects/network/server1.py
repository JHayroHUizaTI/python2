#
import socket

mi_socket = socket.socket()
mi_socket.bind('localhost', 8000)
mi_socket.liten(5)

while True:
    conexion, addr = mi_socket.accept()
    print()
    