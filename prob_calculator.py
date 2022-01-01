import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **colors):
        self.colors = colors
        self.draw = self.draw

    @property
    def contents(self):
        lijst = []
        for color, amount in self.colors.items():
            for _ in range(amount):
                lijst.append(color)
        return lijst

    def draw(self, amount):
        list = []
        for i in range(amount):
            if len(self.contents) < 1:
                break
            bla = random.choice(self.contents)
            list.append(bla)
            self.colors[bla] -= 1
        return list

    def __repr__(self) -> str:
        result = "Hat("
        for color, amount in self.colors.items():
            result += color
            result += "=" + str(amount) + ", "
        result = result[:-2]
        return result + ")"

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    lijst = []
    for _ in range(num_experiments):
        hat2 = copy.deepcopy(hat)
        lijst.append(hat2.draw(num_balls_drawn))

    count = 0
    for el in lijst:
        for color, amount in expected_balls.items():
            if el.count(color) < amount:
                break
        else:
            count += 1
    return count / num_experiments

def test_repr():
    hat = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
    assert repr(hat) == 'Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)'

    hat = Hat(red=1, green=1)
    assert len(hat.draw(100)) == 2


if __name__ == '__main__':
    test_repr()