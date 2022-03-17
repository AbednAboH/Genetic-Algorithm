# cross functions class
import random
from settings import *
from numpy import  unique

# given 2 samples(citizens) from the population calculate crossed sample
class cross_types:

    def __init__(self):
        # maps functions to numbers so that we can choose which one to assign
        self.select = {CROSS1: self.one_cross, CROSS2: self.two_cross, UNI_CROSS: self.uniform_cross, PMX_: self.PMX,
                       CX_: self.CX}

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
                object1 = object1[:] + citizen2[i]
                object2 = object2[:] + citizen1[i]
            else:
                object1 = object1[:] + citizen1[i]
                object2 = object2[:] + citizen2[i]
        return object1, object2

    def PMX(self, citizen1, citizen2):
        target_size = len(citizen1)
        # repeat 5 times 
        for j in range(5):
            ipos = random.randint(0, target_size - 1)
            c1 = citizen1[ipos]
            c2 = citizen2[ipos]
            # first mutation
            object1 = citizen1[0:ipos] + [c2] + citizen1[ipos + 1:]
            object2 = citizen2[0:ipos] + [c1] + citizen2[ipos + 1:]

            for i in range(target_size):
                object1[i] = c2 if object1[i] == c1 else c1 if object1[i] == c2 else object1[i]
                object2[i] = c1 if object2[i] == c2 else c2 if object2[i] == c1 else object2[i]

        return object1, object2
    # problem accures when cyrcle is broken !
    def CX(self, citizen1, citizen2):
        object1 = citizen1
        object2 = citizen2
        target_len = len(citizen1)
        hash1 = {citizen1[i]: i for i in range(target_len)}
        cycles = []
        cycle = []
        all_indexes = []
        # get all cycles
        if len(unique(object1)) - len(object1) != len(unique(object2)) - len(object2):
            print(f"problem doesn't support this type of crossing ! charachters need to be unique ! so that the cycles exist ")
        # find the cycles
        for i in range(target_len):
            # if we havent gone over this cycle then get its members
            if i not in all_indexes:
                self.cycle(hash1, i, citizen1,citizen2, cycle)
                cycles.append(cycle)
                all_indexes = all_indexes[:] + cycle[:]
     
        for i in range(len(cycles)):
            # if current cycle devides by 2 then swap (i+1 because cycles->(1,...n))
            if (i+1) % 2 == 1:
                current_cycle = cycles[i]
                for j in current_cycle:
                # swap the values in this specific cycle  
                    object1[j], object2[j] = object2[j], object1[j]
        return object1, object2

    def cycle(self, hash2, first,c1, c2, cycle):
        num = hash2[c2[first]]
        cycle.append(num)
        while num != first:
            num = hash2[c2[num]]
            cycle.append(num)
