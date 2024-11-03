import socket

from socket_utils import *
from constants import HOST, PORT, NEW_GAME_HINT, INPUT_HINT, EXIT

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
with sock:
    while True:
        message = recv_msg(sock)
        if message == NEW_GAME_HINT:
            action = input(message)
            send_msg(sock, action)
            if action == 'q':
                print(EXIT)
                break
        elif message == INPUT_HINT:
            while True:
                try:
                    c = tuple(map(int, input(message).split()))
                    send_msg(sock, c)
                    break
                except ValueError:
                    ...
        else:
            print(message)
