import copy
import random

class Hat:
    def __init__(self, **kwargs) -> None:
        self.contents = []

        if kwargs == {}:
            kwargs["black"] = 4

        for k,v in kwargs.items():
            for i in range(0, v):
                self.contents.append(k)
        print(f'Inital ball count: {self.contents}\n')

    def draw(self, draw_count):
        drawn_balls = []
        for i in range(0, draw_count):
            choice = self.contents.pop(random.randrange(0, len(self.contents)))
            drawn_balls.append(choice)
        print(f'Balls drawn: {drawn_balls}')
        print(f'Balls left: {self.contents}')

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass

hat = Hat(yellow=3, blue=2, green=6)
hat.draw(4)