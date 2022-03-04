import math
import random
from datetime import datetime
import secrets
import numpy as np
import time
from ctypes import CDLL
from create_problem_sets import DNA

RAND_MAX = 0x7fff

GA_POPSIZE = 2048
GA_MAXITER = 16384
GA_ELITRATE = 0.10
GA_MUTATIONRATE = 0.25
GA_MUTATION = RAND_MAX * GA_MUTATIONRATE
GA_TARGET = "Hello world!"
TAR_size = len(GA_TARGET)
""" class for our population has a string and a fitness value"""


# will be removed !!!!

class Ga_struct():
    def __init__(self):
        self.object = ""
        self.fitness = 0

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __le__(self, other):
        return self.fitness <= other.fitness

    def __eq__(self, other):
        return self.fitness == other.fitness


""" to generalize the problem we created a class that given a population calculates the solution"""


# given 2 samples(citizens) from the population calculate crossed sample
class cross_types:

    def __init__(self):
        # maps functions to numbers so that we can choose which one to assign
        self.select = {1: self.one_cross, 2: self.two_cross, 3: self.uniform_cross}

    def one_cross(self, citizen1, citizen2):
        target_size = len(citizen1)
        spos = random.randint(0, target_size)
        return citizen1[0:spos] + citizen2[spos:target_size], citizen2[0:spos] + citizen1[spos:target_size]

    def two_cross(self, citizen1, citizen2):
        target_size = len(citizen1)
        spos = random.randint(0, target_size - 2)  # we need at least 3 portions
        spos2 = random.randint(spos, target_size - 1)  # we need at least 2 portions
        first = citizen1[0:spos] + citizen2[spos:spos2] + citizen1[spos2 :]
        sec = citizen2[0:spos] + citizen1[spos:spos2] + citizen2[spos2:]
        return first, sec

    def uniform_cross(self, citizen1, citizen2):
        target_size = len(citizen1)
        object1 = []
        object2 = []
        for i in range(target_size):
            if random.random() > 0.5:
                object1.append(citizen2[i])
                object2.append(citizen1[i])
            else:
                object1.append(citizen1[i])
                object2.append(citizen2[i])
        return object1, object2


class genetic_algorithem:
    def __init__(self, target, tar_size, pop_size, problem_spec, crosstype):
        self.population = list(range(pop_size))
        self.buffer = list(range(pop_size))
        self.target = target
        self.target_size = tar_size
        self.pop_size = pop_size
        self.pop_mean = 0
        self.iteration = 0  # current iteration that went through the algorithem
        self.prob_spec = problem_spec
        self.file = open(r"pres.txt", "w+")
        self.cross_func = cross_types().select[crosstype]

    def init_population(self, pop_size, target_size):

        for i in range(pop_size):
            citizen = self.prob_spec()
            citizen.create_object(target_size)
            citizen.calculate_fittness(self.target, target_size)
            self.population[i] = citizen

    # this function calculates fittness for all the population and it's mean value and returns it """

    def calc_fitness(self):
        mean = 0
        for i in range(self.pop_size):
            self.population[i].calculate_fittness(self.target, self.target_size)
            mean += self.population[i].fitness

        self.pop_mean = mean / self.pop_size

    def sort_by_fitness(self):
        self.population.sort()

    def elitism(self, esize):
        for i in range(esize):
            self.buffer[i] = self.population[i]

    def mutate(self, member):
        member.mutate(self.target_size, member)

    def mate(self):
        esize = math.floor(self.pop_size * GA_ELITRATE)
        self.elitism(esize)
        self.cross()

    def cross(self):

        for i in range(self.pop_size):
            self.buffer[i] = self.prob_spec()
            citizen1= self.prob_spec()
            citizen2= self.prob_spec()
            i1 = random.randint(0, self.pop_size // 2)
            i2 = random.randint(0, self.pop_size // 2)
            # spos = random.randint(0, self.target_size)
            # # self.buffer[i] = Ga_struct()
            # self.buffer[i].object = self.population[i1].object[0:spos] + self.population[i2].object[spos:]
            citizen1.object, citizen2.object = self.cross_func(self.population[i1].object, self.population[i2].object)
            citizen1.calculate_fittness(self.target,self.target_size)
            citizen2.calculate_fittness(self.target,self.target_size)
            self.buffer[i]=citizen1 if citizen1.fitness<citizen2.fitness else citizen2

            if (secrets.randbelow(122) < GA_MUTATION):
                self.mutate(self.buffer[i])

    def get_levels_fitness(self):
        arr = {}
        for i in self.population:
            if i.fitness in arr.keys():
                arr[i.fitness] += 1
            else:
                arr[i.fitness] = 1
        for i in arr.keys():
            self.file.write(str(i) + " " + str(arr[i]) + "\n")

    def solve_genetic_problem(self):
        tick = time.time()
        sol_time = time.perf_counter()
        # random.seed(datetime.now())
        self.init_population(self.pop_size, self.target_size)
        # for i in self.population:
        #     print(i.object)
        for i in range(GA_MAXITER):
            self.file.write("i" + str(self.iteration) + "\n")

            self.iteration += 1

            self.calc_fitness()  # // calculate fitness

            self.sort_by_fitness()

            self.get_levels_fitness()

            runtime = time.perf_counter() - sol_time
            clockticks = time.time() - tick
            print_B(self.population)
            print_mean_var((self.pop_mean, variance((self.pop_mean, self.population[0].fitness))))
            print_time((runtime, clockticks))
            if (self.population)[0].fitness == 0: break

            self.mate()  # // mate the population together

            self.population, self.buffer = self.buffer, self.population  # // swap buffers
        self.file.close()
        return 0


# inline functions


# that prints the best candidate

print_B = lambda x: print(f" Best: {x[0].object} ,fittness: {x[0].fitness} ", end=" ")

#  prints mean and variance
print_mean_var = lambda x: print(f"Mean: {x[0]} ,Variance: {x[1]}", end=" ")
# prints time
print_time = lambda x: print(f"Time :  {x[0]}  ticks: {x[1]}")
# calculates variance
variance = lambda x: math.sqrt((x[0] - x[1]) ** 2)


# no need !!!!!


def main():
    overall_time = time.perf_counter()
    GA = genetic_algorithem(GA_TARGET, TAR_size, GA_POPSIZE, DNA, 2)
    GA.solve_genetic_problem()
    overall_time = time.perf_counter() - overall_time


if __name__ == "__main__":
    main()
