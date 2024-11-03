from typing import List

class Tic_Tac_Toe():
    game_field = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ]
    
    cur_player = 1
    prev_player = -1
    
    def __init__(self):
        self.game_field = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
            ]
        self.cur_player = 1
        self.prev_player = -1

    def set_cell(self, row: int, column: int) -> int:
        if 0 <= row <= 2 and 0 <= column <= 2 and self.game_field[row][column] == 0:
            self.game_field[row][column] = self.cur_player
            self.prev_player = self.cur_player
            self.cur_player = (self.cur_player//2)+(self.cur_player%2)*2
            return 0
        return -1
    
    def get_field(self) -> List[List[int]]:
        return self.game_field

    def print_field(self) -> str:
        res = ''
        for row in self.get_field():
            for column in row:
                res += f'{column} '
            res += '\n'
        return res

    def reset_field(self) -> None:
        self.game_field = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
        ]
        
        self.cur_player = 1
        self.prev_player = -1
    
    def get_cur_player(self) -> int:
        return self.cur_player

    def get_prev_player(self) -> int:
        return self.prev_player
    
    def check_win(self, player: int) -> bool:
        if self.game_field[0].count(player) == 3:
            return True
        elif self.game_field[1].count(player) == 3:
            return True
        elif self.game_field[2].count(player) == 3:
            return True
        elif self.game_field[0][0] == self.game_field[1][0] == self.game_field[2][0] == player:
            return True
        elif self.game_field[0][1] == self.game_field[1][1] == self.game_field[2][1] == player:
            return True
        elif self.game_field[0][2] == self.game_field[1][2] == self.game_field[2][2] == player:
            return True
        elif self.game_field[0][0] == self.game_field[1][1] == self.game_field[2][2] == player:
            return True
        elif self.game_field[0][2] == self.game_field[1][1] == self.game_field[2][0] == player:
            return True
        else:
            return False
        
    def check_draw(self) -> bool:
        if self.game_field[0].count(0) == self.game_field[1].count(0) == self.game_field[2].count(0) == 0:
            return True
        else:
            return False
