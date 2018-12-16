white = 0
black = 1
board_size = 8
class ReversiBoard(object):
    def __init__(self):
        self.cells = []
        for i in range(board_size):
            self.cells.append([None for i in range(board_size)])
        self.cells[3][3] = white
        self.cells[3][4] = black
        self.cells[4][3] = black
        self.cells[4][4] = white

    def put_stone(self,x,y,player):
        if self.cells[y][x] != None:
            return False
        getable = self.list_getable_stones(x,y,player)
        if len(getable)==0:
            return False
        self.cells[y][x] = player
        for x,y in getable:
            self.cells[y][x] = player
        return True

    def list_getable_stones(self,x,y,player):
        Previo = -1
        Next = 1
        Direction = [Previo,0,Next]
        getable=[]
        for dx in Direction:
            for dy in Direction:
                if dx == 0 and dy == 0:
                    continue
                tmp = []
                Depth = 0
                while True:
                    Depth+=1
                    rx = x + (dx * Depth)
                    ry = y + (dy * Depth)
                    if 0 <= rx < board_size and 0 <= ry < board_size:
                        req = self.cells[ry][rx]
                        if req == None:
                            break
                        if req == player:
                            if len(tmp) == 0:
                                getable.extend(tmp)
                        else:
                            tmp.append((rx,ry))
                    else:
                        break
        return getable

    def show_board(self):
        print('--'*15)
        for i in self.cells:
            for cell in i:
                if cell == white:
                    print('W',end = "")
                elif cell == black:
                    print('B',end = "")
                else:
                    print('*',end = "")
            print('\n',end = '')

    def list_possible_cells(self,player):
        possible = []
        for x in range(board_size):
            for y in range(board_size):
                if self.cells[y][x] != None:
                    continue
                if self.list_getable_stones(x,y,player) == []:
                    continue
                else:
                    possible.append((x,y))
        return possible


class Game(ReversiBoard):
    Draw = -1

    def __init__(self,turn = 0,start_player=black):
        super().__init__()
        self.player = start_player
        self.turn = turn
        self.winner = None
        self.was_passed = False

    def finished(self):
        return self.winner != None

    def list_possible_cells(self):
        return super().list_possible_cells(self.player)

    def get_color(self,player):
        if player == white:
            return 'white'
        elif player == black:
            return 'black'
        else:
            return 'Draw'

    def get_current_player(self):
        return self.player

    def get_next_player(self):
        return white if self.player == black else black

    def shift_player(self):
        self.player = self.get_next_player()

    def put_stone(self,x,y):
        if super().put_stone(x,y,player):
            self.was_passed = False
            self.player = self.get_next_player()
            self.turn += 1
        else:
            return False

    def pass_moving(self):
        if self.was_passed:
            return self.finish_game()

        self.was_passed = True
        self.shift_player()

    def print_score(self):
        print('{}: {}'.format('black',self.stones[black]))
        print('{}: {}'.format('white',self.stones[white]))

    def finish_game(self):
        self.stones = self.get_stone_map()
        white = self.stones[white]
        black = self.stones[black]
        if white < black:
            self.winner = black
        elif black < white:
            self.winner = white
        else:
            self.winner = self.on_draw()

    def on_draw(self):
        return self.Draw


if __name__ == "__main__":
    game=Game()
    while True:
        possible = game.list_possible_cells()
        player_name = game.get_color(game.get_current_player())
        if game.finished():
            game.show_board()
            game.print_score()
            print('Winner: {}'.format(game.get_color(game.winner)))
            break
        if len(possible) == 0:
            print('Player {} can not put'.format(player_name))
            game.pass_moving()
            continue
        game.show_board()
        print('Player: {}'.format(player_name))
        print('put to: {}'.format(str(possible)))
        index = int(input('choose: '))
        game.put_disk(*possible[index])
