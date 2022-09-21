from inspect import BoundArguments
from random import Random as rand
import re
class Dice:
    def __init__(self, description) -> None:
        self.parts = description.split('d')
        mod = self.parts[1].split('+')
        self.parts[1] = mod[0]
        self.parts = [int(self.parts[0]), int(self.parts[1])]
        self.bonus = 0
        self.rolls = []
        if(len(mod) > 1):
            self. bonus = int(mod[1])
        self.process()

    def process(self):
        for i in range(int(self.parts[0])):
            num = self.rollOnce()
            self.rolls.append(num)
        
    def value(self):
        return sum(self.rolls) + self.bonus
    def dropLowest(self):
        val = min(self.rolls)
        self.parts[0] -= 1
        self.rolls.pop(self.rolls.index(val))
    def max(self):
        return (int(self.parts[0]) * int(self.parts[1])) + self.bonus
    def rollOnce(self):
        return rand().randrange(1, int(self.parts[1]) + 1)
    def rerollOnesCont(self):
        while 1 in self.rolls:
            self.rerollOnesOnce()
    def rerollOnesOnce(self):
        for roll in self.rolls:
            if roll == 1:
                self.rolls[self.rolls.index(roll)] = self.rollOnce()
        

if __name__ == "__main__":
    dice = ["6d6", "3d4+8", "4d6", "12d6", "8d6"]
    for die in dice:
        d = Dice(die)
        match dice.index(die):
            case 2:
                d.dropLowest()
            case 3:
                d.rerollOnesCont()
            case 4:
                d.rerollOnesOnce()
        
        print(d.value(), d.max())