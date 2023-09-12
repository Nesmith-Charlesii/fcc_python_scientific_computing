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
        if draw_count > len(self.contents):
            return self.contents
        
        balls_drawn = []
        for i in range(0, draw_count):
            choice = self.contents.pop(random.randrange(0, len(self.contents)))
            balls_drawn.append(choice)
        print(f'Balls drawn: {balls_drawn}')
        print(f'Balls left: {self.contents}')
        return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hat_copy = copy.copy(hat)
    expected_ball_list = []

    # First create a list of expected balls from expected_balls dict
    for k,v in expected_balls.items():
        for i in range(0, v):
            expected_ball_list.append(k)

    balls_drawn = hat_copy.draw(5)



hat1 = Hat(yellow=3, blue=2, green=6)
#hat1.draw(4)
experiment(
    hat=hat1,
    expected_balls={"red": 2, "green": 1},
    num_balls_drawn=5,
    num_experiments=2000
)