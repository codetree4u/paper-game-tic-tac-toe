class Board:
    def __init__(self):
        self.board = [' ', ' ', ' ', 
                      ' ', ' ', ' ', 
                      ' ', ' ', ' ']
 
    def print_board(self):
        print('\n')
        print(' ' + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        print('-----------')
        print(' ' + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print('-----------')
        print(' ' + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])
 
class Player:
    def __init__(self, type):
        self.type = type
        self.name = self.get_name()
    
    def get_name(self):
        if self.type == 'X':
            name = input('Player selecting X, enter your name: ')
        else:
            name = input('Player selecting O, enter your name: ')
        return name
 
class Game:
    def __init__(self):
        self.board = Board()
 
        self.player1 = Player('X')
        self.player2 = Player('O')
 
        self.current_player = self.player1
 
    # this method will be later used to play the game
    def play(self):
         pass
 
game = Game()
game.play()
