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
        else: 
            balls_drawn = []
            for i in range(0, draw_count):
                balls_taken = self.contents.pop(random.randrange(0, len(self.contents)))
                balls_drawn.append(balls_taken)

            return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    match_count = 0
    balls_found = {}
    print(f'Expected balls ---> {expected_balls}\n')
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        for k,v in expected_balls.items():
            if balls_drawn.count(k) >= v:
                balls_found[k] = v
                print(f'Balls found: {balls_found}')
                match_count += 1 if balls_found == expected_balls else 0

    print(f'match_count: {match_count}/{num_experiments}\nprobability: {match_count/num_experiments}')
    return match_count/num_experiments

hat1 = Hat(blue=3,red=2,green=6)
#hat1.draw(4)
experiment(
    hat=hat1,
    expected_balls={"blue":2,"green":1},
    num_balls_drawn=4,
    num_experiments=4
)