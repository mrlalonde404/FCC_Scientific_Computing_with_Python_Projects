import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            for _ in range(v):
                self.contents.append(k)

    def draw(self, num_balls):
        rand_balls = []
        if num_balls == 0:
            return rand_balls
        for i in range(num_balls):
            # generate a random # to grab a random ball
            rand_num = random.randint(0, len(self.contents) - 1)
            # draw without replacement
            rand_balls.append(self.contents.pop(rand_num))
        return rand_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for i in range(num_experiments):
        # get a copy of the original contents of the hat
        cp = copy.deepcopy(hat)
        # draw the number of balls and see if drawn is the same as expected if they are then increment M by 1
        drawn = cp.draw(num_balls_drawn)
        success = True
        for key in expected_balls.keys():
            if drawn.count(key) < expected_balls[key]:
                success = False
                break
        if success:
            M += 1
    # the final probability is M over the number of experiments
    print("experiments done")
    return M / num_experiments


def main():
    hat = Hat(blue=3, red=2, green=6)
    probability = experiment(hat=hat, expected_balls={"blue": 2, "green": 1}, num_balls_drawn=4, num_experiments=1000)
    actual = probability
    print(actual)
    expected = 0.272


if __name__ == '__main__':
    main()
