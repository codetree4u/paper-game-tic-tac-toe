class Board:
    def __init__(self):
        self.board = [' ', ' ', ' ', 
                      ' ', ' ', ' ', 
                      ' ', ' ', ' ']
 
    # method to print the board
    def print_board(self):
        print('\n')
        print(' ' + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        print('-----------')
        print(' ' + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print('-----------')
        print(' ' + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])
 
 
# create an object of Board for testing
board = Board()
board.print_board()
