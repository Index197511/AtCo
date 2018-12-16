import sys
WHITE = 0
BLACK = 1
BOARD_SIZE = 8
class ReversiBoard(object):
    def __init__(self):

        self.cells = []
        for i in range(BOARD_SIZE):
            self.cells.append([None for i in range(BOARD_SIZE)])


        self.cells[3][3] = WHITE
        self.cells[3][4] = BLACK
        self.cells[4][3] = BLACK
        self.cells[4][4] = WHITE

    def put_disk(self, x, y, player):

        if self.cells[y][x] is not None:
            return False


        flippable = self.list_flippable_disks(x, y, player)
        if flippable == []:
            return False


        self.cells[y][x] = player
        for x,y in flippable:
            self.cells[y][x] = player

        return True

    def list_flippable_disks(self, x, y, player):

        PREV = -1
        NEXT = 1
        DIRECTION = [PREV, 0, NEXT]
        flippable = []

        for dx in DIRECTION:
            for dy in DIRECTION:
                if dx == 0 and dy == 0:
                    continue

                tmp = []
                depth = 0
                while(True):
                    depth += 1

                    rx = x + (dx * depth)
                    ry = y + (dy * depth)


                    if 0 <= rx < BOARD_SIZE and 0 <= ry < BOARD_SIZE:
                        request = self.cells[ry][rx]


                        if request is None:
                            break

                        if request == player:
                            if tmp != []:
                                flippable.extend(tmp)
                            break
                        else:

                            tmp.append((rx, ry))
                    else:
                        break
        return flippable
    def show_board(self):

        print("--" * 20)
        print('  0 1 2 3 4 5 6 7')
        j=0
        for i in self.cells:
            print("{} ".format(j),end="")
            for cell in i:
                if cell == WHITE:
                    print("W", end=" ")
                elif cell == BLACK:
                    print("B", end=" ")
                else:
                    print("*", end=" ")
            print("\n", end="")
            j+=1
    def list_possible_cells(self, player):

        possible = []
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                if self.cells[y][x] is not None:
                    continue
                if self.list_flippable_disks(x, y, player) == []:
                    continue
                else:
                    possible.append((x, y))
        return possible
class Game(ReversiBoard):
    DRAW = -1

    def __init__(self, turn=0, start_player=BLACK):
        super().__init__()
        self.player = start_player
        self.turn = turn
        self.winner = None
        self.was_passed = False

    def is_finished(self):
        return self.winner is not None

    def list_possible_cells(self):
        return super().list_possible_cells(self.player)

    def get_color(self, player):
        if player == WHITE:
            return "WHITE"
        if player == BLACK:
            return "BLACK"
        else:
            return "DRAW"

    def get_current_player(self):
        return self.player

    def get_next_player(self):
        return WHITE if self.player == BLACK else BLACK

    def shift_player(self):
        self.player = self.get_next_player()

    def put_disk(self, x, y):
        if super().put_disk(x, y, self.player):
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

    def finish_game(self,Winner):
        if Winner == 'Black':
            print('The winner is Black!!')
        elif Winner == 'White':
            print('The winner is White!!')
        else:
            print('It is a draw...')


    def on_draw(self):

        return self.DRAW

    def Exit_conditions(self):
        whi = 0
        bla = 0
        for i in self.cells:
            for cell in i:
                if cell == WHITE:
                    whi += 1
                elif cell == BLACK:
                    bla += 1
                else:
                    pass
        if whi + bla == 64:
            if bla < whi:
                winner = 'White'
            elif bla > whi:
                winner = 'Black'
            else:
                winner = 'Draw'
            return winner
        else:
            return 1

if __name__ == "__main__":
    i = 1
    game = Game()
    while(True):
        possible = game.list_possible_cells()
        player_name = game.get_color(game.get_current_player())

        if game.Exit_conditions() != 1:
            game.show_board()
            Winner = game.Exit_conditions()
            game.finish_game(Winner)
            sys.exit()
        if possible == []:
            print("player {} can not puts.".format(player_name))
            game.pass_moving()
            continue

        game.show_board()
        print("player: " + player_name)
        print('turn: {}'.format(i))
        i+=1
        print("put to: " + str(possible))
        print("please choose anything you like from these")
        while True:
            index = int(input("choose: "))-1

            if 0 <= index < len(possible):
                break
            else:
                print("please choose again")
        game.put_disk(*possible[index])
