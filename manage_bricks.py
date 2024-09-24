from brick import Brick

class BrickManager:
    def __init__(self):
        self.bricks = []

    def create_bricks(self):
        for x in range(-380, 380, 42):
            for y in range(28, 160, 22):
                b = Brick((x, y))
                self.bricks.append(b)

    def check_collision(self, ball):
        for b in self.bricks:
            if b.distance(ball) < 30:
                return True, b
        return False, None
    
    def remove_brick(self, b):
        b.remove()
        self.bricks.remove(b)

