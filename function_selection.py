# cross functions class
import random
from settings import *

# given 2 samples(citizens) from the population calculate crossed sample
class cross_types:

    def __init__(self):
        # maps functions to numbers so that we can choose which one to assign
        self.select = {CROSS1: self.one_cross, CROSS2: self.two_cross, UNI_CROSS: self.uniform_cross}

    def one_cross(self, citizen1, citizen2):
        target_size = len(citizen1)
        spos = random.randint(0, target_size)
        return citizen1[0:spos] + citizen2[spos:target_size], citizen2[0:spos] + citizen1[spos:target_size]

    def two_cross(self, citizen1, citizen2):
        target_size = len(citizen1)
        spos = random.randint(0, target_size - 2)  # we need at least 3 portions
        spos2 = random.randint(spos, target_size - 1)  # we need at least 2 portions
        first = citizen1[0:spos] + citizen2[spos:spos2] + citizen1[spos2:]
        sec = citizen2[0:spos] + citizen1[spos:spos2] + citizen2[spos2:]
        return first, sec

    def uniform_cross(self, citizen1, citizen2):
        target_size = len(citizen1)
        object1 = []
        object2 = []
        for i in range(target_size):
            if random.random() > 0.5:
                object1 += citizen2[i]
                object2 += (citizen1[i])
            else:
                object1 += (citizen1[i])
                object2 += (citizen2[i])
        return object1, object2

#
