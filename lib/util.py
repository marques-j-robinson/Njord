class BaseGrid:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.seen = ['0,0']

    def add_seen(self):
        if self.has_seen() is False:
            self.seen.append(self.get_coord())

    def has_seen(self):
        coord = self.get_coord()
        return coord in self.seen

    def get_coord(self):
        return f'{self.x},{self.y}'

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)

    def up(self):
        self.y += 1

    def right(self):
        self.x += 1

    def down(self):
        self.y -= 1

    def left(self):
        self.x -= 1
