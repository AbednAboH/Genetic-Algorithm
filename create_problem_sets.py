import random
import sys
from numpy import unique

from settings import PENALTY, HIGH_PENALTY

# class for fitness functions , add your fitness function here !
class fitness_selector:
    def __init__(self):
        self.select = {0: self.distance_fittness, 1: self.bul_pqia,2: self.n_queens_conflict}

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
        conflicts=0
        for col in range(target_size):
            for row in range(target_size):
                if row!=col:
                    # check if more than one queen is on the same right diagonal "/"
                    conflicts+=1 if abs(row-col)==abs(object[col]-object[row]) else 0
        # check for duplicates ! ,cannot be detected by diagonal's
        conflicts+=abs(len(unique(object))-len(object))

        return conflicts


    ## fitness for pso

# class for mutations !!

class mutations:
    def __init__(self):
        self.select = {1: self.random_mutate, 2: self.swap_mutate ,3: self.insertion_mutate}
    
    def random_mutate(self, target_size, member,character_creation):
        ipos = random.randint(0, target_size - 1)
        delta = character_creation(target_size)
        member.object = member.object[:ipos] + [delta] + member.object[ipos + 1:]
    def swap_mutate(self, target_size, member,character_creation):
        ipos = random.randint(0, target_size - 2)
        ipos2 = random.randint(ipos + 1, target_size - 1)
        member.object = member.object[0:ipos] + [member[ipos2]] + member.object[ipos + 1:ipos2] + [member[ipos]] + member[ipos2 + 1:]
    def insertion_mutate(self, target_size, member,character_creation):
        ipos = random.randint(0, target_size - 2)
        ipos2 = random.randint(ipos + 1, target_size - 1)
        member.object = member.object[0:ipos] + member.object[ipos + 1:ipos2] + [member[ipos]] + member[ipos2 + 1:]

# basic class for all problem sets because fittness and the member of the population are problem specific
# and we have to eliminate problem specifc parameters from the Genetic algorithem
# might add mutate !
class parameters:
    def __init__(self):
        self.fitnesstype = fitness_selector().select
        self.object = None
        self.age = 0
        self.fitness = 0

    # creates a member of the population
    def create_object(self, target_size):
        return self.object
    def character_creation(self,target_size):
        pass
    # function to calculate the fitness for this specific problem
    def calculate_fittness(self, target, target_size, select_fitness, age_update=True):
        self.fitness = self.fitnesstype[select_fitness](self.object, target, target_size)
        self.age += 1 if age_update else 0
        return self.fitness

    def helper(self, target_size):
        pass

    # for sorting purposes
    def __lt__(self, other):
        return self.fitness < other.fitness

    def __eq__(self, other):
        self.fitness = other.fitness
        self.object = other.object
        # age ! 


# class for first problem
class DNA(parameters):
    mutation=mutations()
    def __init__(self):
        parameters.__init__(self)

    def create_object(self, target_size):
        self.object = []
        for j in range(target_size):
            self.object += [self.character_creation(target_size)]
        self.helper(target_size)
        return self.object

    def character_creation(self,target_size):
        return chr((random.randint(0, 90)) + 32)

    def mutate(self, target_size, member,mutation_type):
        # ipos = random.randint(0, target_size - 1)
        # delta = self.character_creation(target_size)
        # member.object = member.object[:ipos] + [delta] + member.object[ipos + 1:]
        self.mutation.select[mutation_type](target_size, member,self.character_creation)


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

    def create_object(self, target_size):
        self.object = random.sample(range(0, target_size), target_size)
    def character_creation(self,target_size):
        return random.randint(0,target_size-1)

