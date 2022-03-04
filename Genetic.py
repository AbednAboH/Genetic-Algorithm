import math
import random
from datetime import datetime
import secrets
import numpy as np
import time
from ctypes import CDLL
from create_problem_sets import DNA
RAND_MAX = 0x7fff
# libc = CDLL(name="libc.so.6")
GA_POPSIZE = 2048  # ga population size
GA_MAXITER = 16384  # // maximum iterations
GA_ELITRATE = 0.10  # // elitism rate
GA_MUTATIONRATE = 0.25  # // mutation rate
GA_MUTATION = RAND_MAX * GA_MUTATIONRATE
GA_TARGET = "Hello world!"
TAR_size = len(GA_TARGET)
# GA_TARGET = "HI !"

""" class for our population has a string and a fitness value"""


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


class genetic_algorithem:
    def __init__(self, target, tar_size,pop_size, problem_spec):
        self.population = list(range(pop_size))
        self.buffer = list(range(pop_size))
        self.target = target
        self.target_size = tar_size
        self.pop_size = pop_size
        self.pop_mean = 0
        self.iteration = 0  # current iteration that went through the algorithem
        self.prob_spec=problem_spec

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
            self.population[i].calculate_fittness(self.target,self.target_size)
            mean += self.population[i].fitness
        self.pop_mean = mean / self.pop_size

    def sort_by_fitness(self):
        self.population.sort()

    def elitism(self, esize):
        for i in range(self.pop_size):
            self.buffer[i] = self.population[i]

    def mutate(self, member):
        member.mutate(self.target_size,member)

    def mate(self, cross_type):
        esize = math.floor(self.pop_size * GA_ELITRATE)
        self.elitism(esize)
        self.cross(cross_type)

    def cross(self, cross_type):
        for i in range(self.pop_size):
            i1 = random.randint(0, GA_POPSIZE // 2)
            i2 = random.randint(0, GA_POPSIZE // 2)
            spos = random.randint(0, self.target_size)
            # self.buffer[i] = Ga_struct()
            self.buffer[i] = self.prob_spec()
            self.buffer[i].object = self.population[i1].object[0:spos] + self.population[i2].object[spos:]
            if (secrets.randbelow(122) < GA_MUTATION):
                self.mutate(self.buffer[i])

    def solve_genetic_problem(self):

        tick = time.time()
        sol_time = time.perf_counter()
        # random.seed(datetime.now())
        self.init_population(self.pop_size, self.target_size)
        for i in range(GA_MAXITER):

            self.calc_fitness()  # // calculate fitness

            self.sort_by_fitness()
            runtime = time.perf_counter() - sol_time
            clockticks = time.time() - tick
            print_B(self.population)
            print_mean_var((self.pop_mean, variance((self.pop_mean, self.population[0].fitness))))
            print_time((runtime, clockticks))
            if (self.population)[0].fitness == 0: break

            self.mate(0)  # // mate the population together

            self.population, self.buffer = self.buffer, self.population  # // swap buffers
        return 0


# inline functions


# that prints the best candidate

print_B = lambda x: print(f" Best: {x[0].object} ,fittness: {x[0].fitness} ", end=" ")

#  that prints the best candidate
print_mean_var = lambda x: print(f"Mean: {x[0]} ,Variance: {x[1]}", end=" ")
print_time = lambda x: print(f"Time :  {x[0]}  ticks: {x[1]}")
variance = lambda x: math.sqrt((x[0] - x[1]) ** 2)


# no need !!!!!


def main():
    overall_time = time.perf_counter()
    GA = genetic_algorithem(GA_TARGET, TAR_size, GA_POPSIZE,DNA)
    GA.solve_genetic_problem()
    overall_time = time.perf_counter() - overall_time


if __name__ == "__main__":
    main()
