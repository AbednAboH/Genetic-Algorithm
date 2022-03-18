import random
import sys
from numpy import unique,setdiff1d

from settings import PENALTY, HIGH_PENALTY,BIN

# have to fill hash table with different keys when getting the command from main
hash_table = {}


# class for fitness functions , add your fitness function here !
class fitness_selector:
    def __init__(self):
        self.select = {0: self.distance_fittness, 1: self.bul_pqia, 2: self.n_queens_conflict,3: self.n_queens_conf_based_on_place,BIN:self.bins_fitness}

    def distance_fittness(self, object, target, target_size):
        fitness = 0
        for j in range(target_size):
            fit = ord(object[j]) - ord(target[j])
            fitness += abs(fit)
        return fitness

    def bul_pqia(self, object, target, target_size):
        fitness = 0
        for i in range(target_size):
            if ord(object[i]) != ord(target[i]):
                fitness += PENALTY if object[i] in target else HIGH_PENALTY
        return fitness

    # fitness for NQueens:
    def n_queens_conflict(self, object, target, target_size):
        conflicts = 0
        for col in range(target_size):
            for row in range(target_size):
                if row != col:
                    # check if more than one queen is on the same right diagonal "/"
                    conflicts += 1 if abs(row - col) == abs(object[col] - object[row]) else 0
        # check for duplicates ! ,cannot be detected by diagonal's
        conflicts += abs(len(unique(object)) - len(object))

        return conflicts

    def n_queens_conf_based_on_place(self, object, row, col):
        conflicts = 0
        for i in range(len(object)):
            if i == col:
                continue
            if (object[i] == row or abs(object[i] - row) == abs(i - col)):
                conflicts += 1
        return conflicts

    def bins_fitness(self, object, target, target_size):
        number_of_bins = len(object)
        capacity = object[0].capacity
        fill_of_ith_bin = [(bin1.fill / capacity) ** 2 for bin1 in object]
        return (sum(fill_of_ith_bin) / number_of_bins)

    ## fitness for pso


# class for mutations !!

class mutations:
    def __init__(self):
        self.select = {1: self.random_mutate, 2: self.swap_mutate, 3: self.insertion_mutate,BIN:self.distroy_mutate}

    def random_mutate(self, target_size, member, character_creation):
        ipos = random.randint(0, target_size - 1)
        delta = character_creation(target_size)
        member.object = member.object[:ipos] + [delta] + member.object[ipos + 1:]

    def swap_mutate(self, target_size, member, character_creation):
        ipos = random.randint(0, target_size - 2)
        ipos2 = random.randint(ipos + 1, target_size - 1)
        member.object = member.object[:ipos] + [member.object[ipos2]] + member.object[ipos + 1:ipos2] + [
            member.object[ipos]] + member.object[ipos2 + 1:]

    def insertion_mutate(self, target_size, member, character_creation):
        ipos = random.randint(0, target_size - 2)
        ipos2 = random.randint(ipos + 1, target_size - 1)
        member.object = member.object[:ipos] + member.object[ipos + 1:ipos2] + [member.object[ipos]] + member.object[
                                                                                           ipos2:]
    def distroy_mutate(self,target_size,member,character_creation):
        ipos = random.randint(0, len(member.object) -1)
        member.remove_bin(ipos)
        ipos2 = random.randint( 0,len( member.object )-1)
        member.remove_bin(ipos2)
        ipos3=random.randint(0, len(member.object)-1)
        member.remove_bin(ipos3)

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
        self.fitness = self.fitnesstype[select_fitness](self.object, target, target_size)
        self.age += 1 if age_update else 0
        return self.fitness

    def helper(self, target_size):
        pass

    # for sorting purposes
    def __lt__(self, other):
        return self.fitness < other.fitness

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
        self.helper(target_size)
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

    def helper(self, target_size):
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

# bin class for each cromosome contains bins instead of genes
class bin:
    hash = hash_table
    capacity=0
    def __init__(self,capacity,items=[], fill=0):
        self.items = []
        self.fill = 0
        self.capacity=capacity

    def fill_bins(self, items):
        for item in range(len(items)):
            if self.fill + self.hash[items[item]] <= self.capacity:
                self.items.append(items[item])
                self.fill += self.hash[items[item]]
        return setdiff1d(items, self.items)
    def try_to_fill(self,item):
        if not item:
            return False
        if self.fill+self.hash[item]>self.capacity:
            return False
        else:
            self.fill+=self.hash[item]
            self.items.append(item)
            return True

    # if there exists a member that is mutual between the two then return false
    def __lt__(self, other):
        return len(self.items) + len(other.items) != len(unique(other.items + self.items))

    def __eq__(self, other):
        return self.items == other.items


# send target with [real target,capacity of each bin]
class bin_packing_prob(DNA):
    target=[]
    capacity=0
    def __init__(self):
        parameters.__init__(self)
        self.free_items = []
    def target_creater(self,target):
        self.target=target
    def set_capacity(self,cap):
        self.capacity=cap
        bin.capacity=cap
    def remove_bins(self,new_bins):
        # find said bins positions
        current=self.object
        # conflicts=list(len(self.object))
        conflicts=[]
        for orig_bins in current:
            for bins in new_bins:
                # print(bins,orig_bins)
                if bins<orig_bins:
                    # put the different items in a free array for now
                    # self.free_items[:]=self.free_items[:]+setdiff1d(bins,orig_bins)
                    # remove said bins and add new ones
                    conflicts.append((orig_bins,bins))
        for i in self.object:
            if i in conflicts:
                # self.free_items[:]=self.free_items[:]+setdiff1d(bins,orig_bins)

                self.object.remove(i[0])
        # for i in self.object:
        #     if i in conflicts:
        #         self.object.remove(i)
        self.object[:]=self.object[:]+new_bins

        # fill the bins
        self.fill_a_bin(self.target)

    def remove_bin(self,index):
        bin= self.object[index]
        self.object.pop(index)
        # self.free_items=self.free_items[:]+bin.items[:]
        self.free_items=[i for i in self.free_items]+[i for i in bin.items]
        self.fill_a_bin(self.target)

    def fill_a_bin(self,target):
        failed=True
        list2=[item for item in self.free_items]
        for item in list2:
            for bin1 in self.object:
                # try to fill old bins
                if bin1.try_to_fill(item):
                    self.free_items.remove(item)
                    break

        # create new bins for those that weren't added
        # print(self.free_items)
        while(len(self.free_items)):
            new_bin=bin(target[1])
            self.free_items=new_bin.fill_bins(self.free_items)
            self.object[:]+=[new_bin]



    def create_object(self, target_size, target):
        # print(len(self.target[0]),self.capacity)
        obj = random.sample(range(len(self.target[0])), len(self.target[0]))
        self.bin_cappacity = self.target[0]
        self.object = []
        # print(obj)
        while len(obj):
            new_bin=bin(self.capacity)
            obj=new_bin.fill_bins(obj)
            self.object[:] =self.object[:] +[new_bin]


# todo:
# create ways to delete bins /while getting the bins members in free_items without collisions
# fill bins ! using the free items ! , if bins are empty then create a new bin and fill it with the free items !
# crossing and mutations can be done easily after creating above fanctinalities

# important reminder operator < in bins returns false if there exists a common element in 2 bins
# another reminder , each weight has a different key , using hash_table givven in main
