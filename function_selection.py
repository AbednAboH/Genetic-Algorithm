# cross functions class
import random
from settings import *
from numpy import  unique


# given 2 samples(citizens) from the population calculate crossed sample
class cross_types:

    def __init__(self):
        # maps functions to numbers so that we can choose which one to assign
        self.select = {CROSS1: self.one_cross, CROSS2: self.two_cross, UNI_CROSS: self.uniform_cross, PMX_: self.PMX, CX_: self.CX, BIN:self.cross_bin}

    def one_cross(self, citizen1, citizen2):
        target_size =min (len(citizen1.object),len(citizen2.object))
        spos = random.randint(0, target_size)
        return citizen1.object[0:spos] + citizen2.object[spos:target_size], citizen2.object[0:spos] + citizen1.object[spos:target_size]

    def two_cross(self, citizen1, citizen2):
        target_size = min(len(citizen1.object), len(citizen2.object))
        spos = random.randint(0, target_size  - 2)  # we need at least 3 portions
        spos2 = random.randint(spos,  target_size  - 1)  # we need at least 2 portions
        first = citizen1.object[0:spos] + citizen2.object[spos:spos2] + citizen1.object[spos2:]
        sec = citizen2.object[0:spos] + citizen1.object[spos:spos2] + citizen2.object[spos2:]
        return first, sec

    def uniform_cross(self, citizen1, citizen2):
        target_size = min(len(citizen1.object), len(citizen2.object))
        object1 = []
        object2 = []
        for i in range(target_size):
            if random.random() > 0.5:
                object1 = object1[:] + [citizen2.object[i]]
                object2 = object2[:] + [citizen1.object[i]]
            else:
                object1 = object1[:] + [citizen1.object[i]]
                object2 = object2[:] + [citizen2.object[i]]
        return object1, object2

    def PMX(self, citizen1, citizen2):
        target_size =min (len(citizen1.object),len(citizen2.object))
        # repeat 5 times 
        for j in range(5):
            ipos = random.randint(0, target_size - 1)
            c1 = citizen1.object[ipos]
            c2 = citizen2.object[ipos]
            # first mutation
            object1 = citizen1.object[0:ipos] + [c2] + citizen1.object[ipos + 1:]
            object2 = citizen2.object[0:ipos] + [c1] + citizen2.object[ipos + 1:]

            for i in range(target_size):
                object1[i] = c2 if object1[i] == c1 else c1 if object1[i] == c2 else object1[i]
                object2[i] = c1 if object2[i] == c2 else c2 if object2[i] == c1 else object2[i]

        return object1, object2
    # problem accures when cyrcle is broken !
    def CX(self, citizen1, citizen2):
        object1 = citizen1.object
        object2 = citizen2.object
        target_len = min(len(citizen1.object), len(citizen2.object))
        hash1 = {citizen1.object[i]: i for i in range(target_len)}
        cycles = []
        cycle = []
        all_indexes = []
        # get all cycles
        if len(unique(object1)) - len(object1) != len(unique(object2)) - len(object2):
            print(f"problem doesn't support this type of crossing ! characters need to be unique ! so that the cycles exist ")
        # find the cycles
        for i in range(target_len):
            # if we havent gone over this cycle then get its members
            if i not in all_indexes:
                self.cycle(hash1, i, citizen1.object,citizen2.object, cycle)
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

    def cross_bin(self,citizen1, citizen2):
        #two cross over points per chromosom
        c1pos1= random.randint(0,  len(citizen1.object) - 2)
        c1pos2= random.randint(c1pos1+1,  len(citizen1.object)-1)

        c2pos1= random.randint(0,  len(citizen2.object) - 2)
        c2pos2= random.randint(c2pos1+1,  len(citizen2.object)-1)

        c1,c2=citizen1,citizen2

        # crossed_from_c2=[citizen2.object[c2pos1]]+[citizen2.object[c2pos2]]
        # crossed_from_c1=[citizen1.object[c1pos1]]+[citizen1.object[c1pos2]]
        # print(len(crossed_from_c1),len(crossed_from_c2))
        k=10
        crossed_from_c2 = random.sample(citizen2.object, k)
        crossed_from_c1 = random.sample(citizen1.object,k)
        c1.remove_bins(crossed_from_c2)
        c2.remove_bins(crossed_from_c1)
        # print("------------------------",len(c1.object), len(c2.object))
        return c1.object,c2.object
        
        

    def cycle(self, hash2, first,c1, c2, cycle):
        num = hash2[c2[first]]
        cycle.append(num)
        while num != first:
            num = hash2[c2[num]]
            cycle.append(num)


#
# class cross_types_bins(cross_types):
#     def __init__(self):
#         cross_types.__init__(self)
#         # maps functions to numbers so that we can choose which one to assign
#         self.select = {CROSS1: self.one_cross, CROSS2: self.two_cross, UNI_CROSS: self.uniform_cross, PMX_: self.PMX,
#                        CX_: self.CX}
#
#     def one_cross(self, citizen1, citizen2):
#         c1,c2=super().one_cross(citizen1, citizen2)
#
#     def two_cross(self, citizen1, citizen2):
#        c1,c2=super().two_cross(citizen1, citizen2)
#
#     def uniform_cross(self, citizen1, citizen2):
#        c1,c2=super().uniform_cross(citizen1, citizen2)
#
#     def PMX(self, citizen1, citizen2):
#        c1,c2=super().PMX( citizen1, citizen2)
#
#     def CX(self, citizen1, citizen2):
#         c1,c2=super().CX(citizen1, citizen2)
#     def reform_bins(self,c1,c2,o1,o2):
#         pass
#     def find_change(self,c1,o1):
#         pass
#
