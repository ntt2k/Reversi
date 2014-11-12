# Trung Nguyen
# coordinate.py


import othello


class Coordinate:
    def __init__(self, absolute: (int, int), absolute_size: (int, int)):
        ''' Initializes a Coordinate object. '''

        abs_x, abs_y = absolute
        abs_size_x, abs_size_y = absolute_size

        self.point_x = int(abs_x / abs_size_x)
        self.point_y = int(abs_y / abs_size_y)



    def point(self) -> othello.Point:
        ''' Returns a Point(col, row) tuplefor this Coordinate object. '''
        return othello.Point(col=self.point_x, row = self.point_y)



def from_point(absolute: (int, int), absolute_size: (int, int)) -> Coordinate:
    return Coordinate(absolute, absolute_size)
