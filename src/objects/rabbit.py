class Rabbit:
    GRID_CODE = 1

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return "({x}, {y})".format(x=self.x, y=self.y)

    def pos(self):
        return self.x, self.y

    def __eq__(self, value: object) -> bool:
        return self.x == value.x and self.y == value.y

    def __hash__(self):
        return hash((self.x, self.y))
