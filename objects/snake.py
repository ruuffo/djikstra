from PyQt5.QtCore import Qt


class Snake:
    GRID_CODE = 2

    def __init__(self,
                 direction=Qt.Key_Down,
                 body=[(10, 10), (11, 10), (12, 10), (13, 10), (14, 10)]):
        self.direction = direction
        self.body = body

    def change_direction(self, direction):
        self.direction = direction

    def move(self):

        head = self.body[0]
        x, y = head[0], head[1]
        if self.direction == Qt.Key_Left:
            x -= 1
        elif self.direction == Qt.Key_Right:
            x += 1
        elif self.direction == Qt.Key_Down:
            y += 1
        elif self.direction == Qt.Key_Up:
            y -= 1
        new_head = x, y
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        self.body = self.body + [self.body[-1]]
