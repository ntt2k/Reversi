# Trung Nguyen

import collections

Point = collections.namedtuple('Point', 'col row')
Direction = collections.namedtuple('Direction','x y')
directionlst = [Direction(x=0, y=1), Direction(x=1, y=1),
                Direction(x=1, y=0), Direction(x=1, y=-1),
                Direction(x=0, y=-1), Direction(x=-1, y=-1),
                Direction(x=-1, y=0), Direction(x=-1, y=1)]



class OthelloGameState:


    def __init__(self):
        """ OthelloGameState is a class itself that tracks everything important
            about the state of a Othello game as it progresses.  It contains:

             'board', which is a 2-Dimensional list of strings describing
             the game board.  Each string represents one cell on the board
             and is either none, black(X), or white(O).

             'turn', which specifies which player will make the next move;
             its value will always be either black(X) or white(O)."""

        self.none = ' '
        self.black = 'X'
        self.white = 'O'

        self.board_columns = 8  # just default value, have to manually input in new_game_state anyway
        self.board_rows = 8

        self.board = [[str]]
        self.turn = self.black



    ############## PUBLIC FUNCTION #################



    def new_game_state(self,numCol:int,numRow:int,turn:str) -> None:
        """ Set a brand new game """

        # These variables specify the size of the game board
        self.board_columns = numCol
        self.board_rows = numRow

        #Choose which player go first
        # self.turn = choose_player(input('Please choose which player go first? BLACK(X) or WHITE(O) -> ').upper())
        self.turn = turn


        self.board = []

        for c in range(self.board_columns):
            self.board.append([])
            for r in range(self.board_rows):
                self.board[-1].append(self.none)

        self.board[int(self.board_columns/2)][int(self.board_rows/2)] = self.white
        self.board[int(self.board_columns/2)][int(self.board_rows/2)-1] = self.black
        self.board[int(self.board_columns/2)-1][int(self.board_rows/2)-1] = self.white
        self.board[int(self.board_columns/2)-1][int(self.board_rows/2)] = self.black




    def get_point(self, player: str) -> [Point]:
        """ Return a list of point present in the
            current game state of specific player.
            Use to keep track of count.
        """
        pointlst = []
        for c in range(self.board_columns):
            for r in range(self.board_rows):
                if self.board[c][r] == player:
                    pointlst.append(Point(col = c, row = r))
        return pointlst




    def get_possible_move(self) -> [Point]:
        """ Get the possible move for the current turn player """
        resultlst = []
        for i in self.get_point(self.turn):
            resultlst.extend(self._search_sequence_begins_at(i))
        return resultlst





    def make_a_move(self, x: Point) -> None:
        """
        Given a point, returns the game state
        that results when the current player (whose turn it is) place a piece.

        If a move cannot be made in the given column because the column is
        filled already, an InvalidOthelloMoveError is raised.
        """
        if x in self.get_possible_move():
            self.board[x.col][x.row] = self.turn
            self._flip_sequence_begins_at(x)
            self.turn = self._get_opposite_turn()
        else:
            raise InvalidOthelloMoveError()




    def check_game_not_over(self) -> bool:

        """ Raises a OthelloGameOverError if the given game state represents
        a situation where the game is over."""

        if len(self.get_point(self.none)) == 0:
            return False
            # raise OthelloGameOverError()

        elif len(self.get_possible_move()) == 0:
            self.turn = self._get_opposite_turn()   # switch the turn to another player
            if len(self.get_possible_move()) == 0:
                return False
            else:
                return True
                # raise OthelloGameOverError()
        else:
            # pass
            return True


    ############## PRIVATE FUNCTION ################



    def _get_opposite_turn(self) -> str:
        """Given the player whose turn it is now, returns the opposite player"""
        if self.turn == self.white:
            return self.black
        else:
            return self.white




    def _search_sequence_begins_at(self, x: Point) -> [Point]:
        """
        Returns a list of points if search sequence of empty space
        appears on the path extending in any of the
        8 possible directions.
        """
        resultlst = []

        for d in directionlst:
            try:
                n = 1
                while self.board[x.col + d.x * n][x.row + d.y * n] == self._get_opposite_turn():
                    if self._is_valid_column_number(x.col + d.x * (n+1)) and self._is_valid_row_number(x.row + d.y * (n+1)):

                        if self.board[x.col + d.x * (n+1)][x.row + d.y * (n+1)] == self.none:
                            resultlst.append(Point(col=x.col + d.x * (n+1), row=x.row + d.y * (n+1)))
                    n += 1
            except:
                pass
                # print('***Exception!!!*** The game should not end up here! (1)')
        return resultlst




    def _flip_sequence_begins_at(self, x: Point) -> None:
        """ Flip piece in 8 directions and update the current game state
            board according to the specific coordinate. """
        list1 = []

        for d in directionlst:
            try:
                list2 = []
                n = 1
                while self.board[x.col + d.x * n][x.row + d.y * n] == self._get_opposite_turn():

                    list2.append(Point(col=x.col + d.x * n, row=x.row + d.y * n))
                    # print('List 2 -->', list2)  # debug

                    if self._is_valid_column_number(x.col + d.x * (n+1)) and self._is_valid_row_number(x.row + d.y * (n+1)):
                        if self.board[x.col + d.x * (n+1)][x.row + d.y * (n+1)] == self.turn:
                            list1.extend(list2)
                            # print('List 1 -->', list1)  # debug

                    n += 1
            except:
                pass
                # print('***Exception!!!*** The game should not end up here! (2)')
        for i in list1:
            self.board[i.col][i.row] = self.turn




    def _is_valid_column_number(self, column_number: int) -> bool:
        '''Returns True if the given column number is valid; returns False otherwise'''
        return 0 <= column_number < self.board_columns




    def _is_valid_row_number(self, row_number: int) -> bool:
        '''Returns True if the given row number is valid; returns False otherwise'''
        return 0 <= row_number < self.board_rows





### Game Exception Classes ###
class InvalidOthelloMoveError(Exception):
    '''Raised whenever an invalid move is made'''
    # print('Exception: InvalidOthelloMoveError! This move cannot be made! ')
    pass


class OthelloGameOverError(Exception):
    '''
    Raised whenever an attempt is made to make a move after the game is
    already over
    '''
    # print('Exception: OthelloGameOverError!')
    pass









