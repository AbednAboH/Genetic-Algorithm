import random
import sys

from settings import PENALTY, HIGH_PENALTY


class fitness_selector:
    def __init__(self):
        self.select = {0: self.distance_fittness, 1: self.bul_pqia}

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
    ## fitness for pso


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
    def __init__(self):
        parameters.__init__(self)

    def create_object(self, target_size):
        self.object = ""
        for j in range(target_size):
            self.object += chr((random.randint(0, 90)) + 32)
        self.helper(target_size)
        return self.object

    def mutate(self, target_size, member):
        ipos = random.randint(0, target_size - 1)
        delta = random.randint(0, 90) + 32
        member.object.replace(member.object[ipos], chr((ord(member.object[ipos]) + delta) % 122))


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
