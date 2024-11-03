import socket
import struct
import pickle

from typing import Any

def send_msg(conn : socket.socket, msg: Any) -> None:
    send_data = pickle.dumps(msg)
    conn.sendall(struct.pack('>I', len(send_data)))
    conn.sendall(send_data)
    
    
def recv_msg(conn: socket.socket) -> Any:
    data_size = struct.unpack('>I', conn.recv(4))[0]
    recev_data = b''
    remaining_size = data_size
    while remaining_size != 0:
        recev_data += conn.recv(remaining_size)
        remaining_size = data_size - len(recev_data)
    return pickle.loads(recev_data)
