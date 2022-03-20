import random
import sys
from numpy import unique, setdiff1d
from settings import PENALTY, HIGH_PENALTY, BIN
from fitness_functions import fitness_selector,hash_table
from mutations import mutations
# have to fill hash table with different keys when getting the command from main


# basic class for all problem sets because fittness and the member of the population are problem specific
# and we have to eliminate problem specifc parameters from the Genetic algorithem
# might add mutate !
class parameters:
    fitnesstype = fitness_selector().select

    def __init__(self):
        self.object = None
        self.age = 0
        self.fitness = 0

    # creates a member of the population
    def create_object(self, target_size, target):
        return self.object

    def character_creation(self, target_size):
        pass

    # function to calculate the fitness for this specific problem
    def calculate_fittness(self, target, target_size, select_fitness, age_update=True):
        # print(len(self.object))
        self.fitness = self.fitnesstype[select_fitness](self, target, target_size)
        self.age += 1 if age_update else 0
        return self.fitness

    def create_special_parameter(self, target_size):
        pass

    # for sorting purposes
    def __lt__(self, other):
        return self.fitness < other.fitness

    def __str__(self):
        bstr = ""
        for i in self.object:
            bstr += str(i) + " "
        return bstr
    # def __eq__(self, other):
    #     self.fitness = other.fitness
    #     self.object = other.object
    # age !


# class for first problem
class DNA(parameters):
    mutation = mutations()

    def __init__(self):
        parameters.__init__(self)

    def create_object(self, target_size, target):
        self.object = []
        for j in range(target_size):
            self.object += [self.character_creation(target_size)]
        self.create_special_parameter(target_size)
        return self.object

    def character_creation(self, target_size):
        return chr((random.randint(0, 90)) + 32)

    def mutate(self, target_size, member, mutation_type):
        self.mutation.select[mutation_type](target_size, member, self.character_creation)


# class for pso problem
class PSO_prb(DNA):
    # our object is the initial position , we added 2 parameters that are required
    def __init__(self):
        DNA.__init__(self)
        self.velocity = None
        self.p_best = sys.maxsize
        self.p_best_object = None

    def create_special_parameter(self, target_size):
        self.create_velocity(target_size)

    def create_velocity(self, target_size):
        self.velocity = [random.random() for i in range(target_size)]

    def calculate_new_position(self):
        pos = ""
        for i in range(len(self.object)):
            pos += chr((ord(self.object[i]) + int(self.velocity[i])) % 256)
        self.object = pos

    def calculate_velocity(self, c1, c2, gl_best, w=0.5):
        for i in range(len(self.object)):
            cc1 = c1 * (ord(self.p_best_object[i]) - ord(self.object[i])) * random.random()
            cc2 = c2 * (ord(gl_best[i]) - ord(self.object[i])) * random.random()
            self.velocity[i] = self.velocity[i] * w + cc1 + cc2

    def __eq__(self, other):
        DNA.__eq__(self, other)
        self.velocity = other.velocity
        self.best_object = other.best_object

    def __str__(self):
        if self.object == None:
            return ""
        else:
            return super(PSO_prb, self).__str__()


# class to define n queens problem
# approach :  with an array of N places , each place represents the row 
# and the value in each place represents colums meaning : 
# Arr={6,3,...}   ;   Arr[0] is the 6's column and 0 is the row 
class NQueens_prb(DNA):
    def __init__(self):
        parameters.__init__(self)

    def create_object(self, target_size, target=None):
        obj = random.sample(range(target_size), target_size)
        while len(unique(obj)) != len(obj):
            obj = random.sample(range(target_size), target_size)
        self.object = obj

    def character_creation(self, target_size):
        return random.randint(0, target_size - 1)


# bin class for each cromosome that puts items from the cromosome in a bin
class bin:
    hash = hash_table
    capacity = 0

    def __init__(self, capacity, items=[], fill=0):
        self.items = []
        self.fill = 0
        self.capacity = capacity

    def fill_bins(self, items):
        for item in range(len(items)):
            if self.fill + self.hash[items[item]] <= self.capacity:
                self.items.append(items[item])
                self.fill += self.hash[items[item]]
            # else:
            #     break
        return setdiff1d(items, self.items)



    # if there exists a member that is mutual between the two then return false
    def __lt__(self, other):
        return len(self.items) + len(other.items) != len(unique(other.items + self.items))

    def __eq__(self, other):
        return self.items == other.items
# add a field for bins with a way to fill them "first fit "
class first_fit_prob(bin):
    hash = hash_table
    capacity = 0

    def __init__(self, capacity, items=[], fill=0):
        bin.__init__(self,capacity)

    def fill_bins(self, items):
        #fit according to the fill ratio
        for item in range(len(items)):
            if self.fill + self.hash[items[item]] <= self.capacity:
                self.items.append(items[item])
                self.fill += self.hash[items[item]]
        return setdiff1d(items, self.items)

# class bin(first_fit):

# send target with [real target,capacity of each bin]
class bin_packing_prob(DNA):
    target = []
    capacity = 0
    bin1=bin

    def __init__(self):
        parameters.__init__(self)
        self.bin_objects = []

    def target_creater(self, target):
        self.target = target

    def set_capacity(self, cap):
        self.capacity = cap
        self.bin1.capacity = cap

    def create_special_parameter(self, target_size):
        self.bin_objects = []
        obj = self.object
        # print(self)
        while len(obj):
            new_bin = self.bin1(self.capacity)
            obj = new_bin.fill_bins(obj)
            self.bin_objects[:] = self.bin_objects[:] + [new_bin]
        # print(self)

    def create_object(self, target_size, target):
        # print(len(self.target[0]),self.capacity)
        self.object = random.sample(range(len(self.target[0])), len(self.target[0]))
        # self.bin_cappacity = self.target[0]
        self.create_special_parameter(target_size)

    def __str__(self):
        count = 0
        bstr = ""
        for i in self.bin_objects:
            bstr += "["
            for j in i.items:
                count += hash_table[j]
                bstr += str(hash_table[j]) + ","
            bstr += "]"
        bstr += "]\n"
        bstr+="number of bins:"+str(len(self.bin_objects))+"\n"
        return bstr

#first-fit
class bin_pack(bin_packing_prob):
    bin1 = first_fit_prob
    def __init__(self):
        super(bin_pack, self).__init__()




class hybrid_bin_packing_prob(DNA):
    target = []
    capacity = 0

    def __init__(self):
        parameters.__init__(self)
        self.free_items = []

    def target_creater(self, target):
        self.target = target

    def set_capacity(self, cap):
        self.capacity = cap
        bin.capacity = cap

    def remove_bins(self, new_bins):
        # find said bins positions
        current = self.object
        conflicts = [[] for i in range(len(new_bins))]
        unique_conflicts = []

        for bins in range(len(new_bins)):
            for index, orig_bins in enumerate(current):
                if new_bins[bins] < orig_bins:
                    # create a set of conflicts between bins and original bins
                    # i.e bin[x] has conflict with original bin[x,y,z] => conflicts[x]=[x,y,z] => conflicts=[ [] [] [] [] [x,y,z] ]
                    # so that we can differentiate which weights to remove from each original bin
                    conflicts[bins].append(orig_bins)
                    # array of bins that have conflicted sets so that we know which ones to remove
                    if index not in unique_conflicts:
                        unique_conflicts.append(index)
                    # gives back correct output!
        # get the free items here
        # conflict_set_index : new bins number i to compare with conflict set number i
        # works perfectly
        for conflict_set_index in range(len(new_bins)):
            for bin in conflicts[conflict_set_index]:
                self.free_items = list(self.free_items[:]) + list(
                    setdiff1d(bin.items, new_bins[conflict_set_index].items))
        # doesnt remove bins!
        self.free_items = list(unique(self.free_items))
        # print("**********************************************************")
        # print("items ",self.free_items)
        # print("before removing bins ",self)

        self.object = [self.object[i] for i in range(len(self.object)) if i not in unique_conflicts]
        # print("after removing bins ",self)
        # print("**********************************************************")
        #
        # # now we can add the new bins
        # # print("-----------------------------------------------")
        # print("befor adding bins", self)
        self.object[:] = self.object[:] + new_bins
        # print("befor filling bins", self)
        # print("-----------------------------------------------")
        # fill the bins
        self.fill_a_bin(self.target)
        # print("after filling bins", self)
        # print("-----------------------------------------------")

    def remove_bin(self, index):
        bin = self.object[index]
        self.object.pop(index)
        # self.free_items=self.free_items[:]+bin.items[:]
        self.free_items = [i for i in self.free_items] + [i for i in bin.items]
        self.fill_a_bin(self.target)

    def fill_a_bin(self, target):
        failed = True
        list2 = [item for item in self.free_items]
        list2 = sorted(list2, key=lambda x: hash_table[x])
        # list3=[hash_table[i] for i in list2 ]
        # print(list3)
        for item in list2:
            for bin1 in self.object:
                # try to fill old bins
                if bin1.try_to_fill(item):
                    self.free_items.remove(item)
                    break

        # create new bins for those that weren't added
        # print(self.free_items)
        while (len(self.free_items)):
            new_bin = bin(target[1])
            self.free_items = new_bin.fill_bins(self.free_items)
            self.object[:] += [new_bin]

    def create_object(self, target_size, target):
        # print(len(self.target[0]),self.capacity)
        obj = random.sample(range(len(self.target[0])), len(self.target[0]))
        # self.bin_cappacity = self.target[0]
        self.object = []
        # print(obj)
        while len(obj):
            new_bin = bin(self.capacity)
            obj = new_bin.fill_bins(obj)
            self.object[:] = self.object[:] + [new_bin]

    def __str__(self):
        bstr = str(len(self.object)) + "["
        for i in self.object:
            bstr += "["
            for j in i.items:
                bstr += str(j) + ","
            bstr += "]"
        bstr += "]"
        return bstr

    # todo:
# create ways to delete bins /while getting the bins members in free_items without collisions
# fill bins ! using the free items ! , if bins are empty then create a new bin and fill it with the free items !
# crossing and mutations can be done easily after creating above fanctinalities

# important reminder operator < in bins returns false if there exists a common element in 2 bins
# another reminder , each weight has a different key , using hash_table givven in main
