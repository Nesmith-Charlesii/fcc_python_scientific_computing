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

    def __str__(self) -> str:
        return f'{self.contents}'

    def draw(self, draw_count):
        if draw_count > len(self.contents):
            print(f'draw count exceeds amount of balls in hat ***** {self.contents}')
            return self.contents
        
        balls_drawn = []
        for i in range(0, draw_count):
            choice = self.contents.pop(random.randrange(0, len(self.contents)))
            balls_drawn.append(choice)

        return balls_drawn


ball_outcome = {}

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    if num_experiments < 1:
        if ball_outcome == expected_balls:
            print(f'ball_outcome: {ball_outcome}\n** matches **\nexpected_balls: {expected_balls}')
        else: 
            print(f'expected outcome does not match outcome')
    else:
        # Using copy.deepcopy as to not affect the original instance
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)

        for k,v in expected_balls.items():
            if balls_drawn.count(k) == v:
                ball_outcome [k] = v
        
        experiment(hat, expected_balls, num_balls_drawn, num_experiments=num_experiments-1)


hat1 = Hat(black=6, red=4, green=3)
#hat1.draw(4)
experiment(
    hat=hat1,
    expected_balls={"red": 2, "green": 1},
    num_balls_drawn=5,
    num_experiments=3
)