import socket

from game import Tic_Tac_Toe
from socket_utils import *
from constants import HOST, PORT, INPUT_HINT, NEW_GAME_HINT, LOSE, WIN, DRAW, CURRENT_PLAYER_MOVE, PLAYER_EXIT

def check_end_game(game_: Tic_Tac_Toe, sock: socket.socket) -> str:
    if game_.check_win(game_.get_prev_player()) is True:
        if game_.get_prev_player() == 1:
            print(WIN)
            send_msg(sock, LOSE)
        else:
            print(LOSE)
            send_msg(sock, WIN)
        
        send_msg(sock, NEW_GAME_HINT)
        message = recv_msg(sock)
                    
        while message not in ('n', 'q'):
            send_msg(sock, NEW_GAME_HINT)      
            message = recv_msg(sock)
        
        return message
    elif game_.check_draw() is True:
        print(DRAW)
        send_msg(sock, DRAW)
        
        send_msg(sock, NEW_GAME_HINT)
        message = recv_msg(sock)
                    
        while message not in ('n', 'q'):
            send_msg(sock, NEW_GAME_HINT)      
            message = recv_msg(sock)
            
        return message
    
    return ''

def print_info(game_tto: Tic_Tac_Toe, sock: socket.socket) -> str:
    gamefield = game_tto.print_field()
    print(gamefield)
    send_msg(sock, gamefield)
    
    act = check_end_game(game_tto, conn)
    if act != '':
        return act
                
    mess = CURRENT_PLAYER_MOVE.format(game_tto.get_cur_player())
    print(mess)
    send_msg(sock, mess)
    
    return ''

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen(1)
    conn, addr = sock.accept()
    with conn:
        print(f'Успешное подключение к {addr}')
        game_tto = Tic_Tac_Toe()
        while True:
            res = print_info(game_tto, conn)
            if res == 'q':
                print(PLAYER_EXIT.format(addr))
                break
            elif res == 'n':
                game_tto.reset_field()
                print_info(game_tto, conn)
            
            if game_tto.get_cur_player() == 1:
                action = (-1, -1)
                while True:
                    try:
                        while game_tto.set_cell(action[0], action[1]) != 0:
                            action = tuple(map(int, input(INPUT_HINT).split()))
                            if len(action) != 2:
                                action = (-1, -1)
                        break
                    except ValueError:
                        ...
            else:
                action = (-1, -1)
                        
                while game_tto.set_cell(action[0], action[1]) != 0:
                    send_msg(conn, INPUT_HINT)
                    action = recv_msg(conn)
                    if not isinstance(action, tuple) or len(action) != 2:
                        action = (-1, -1)
