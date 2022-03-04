# pragma warning(disable:4786)		// disable debug warning

# include <iostream>					// for cout etc.
# include <vector>					// for vector class
# include <string>					// for string class
# include <algorithm>				// for sort algorithm
# include <time.h>					// for random seed
# include <math.h>					// for abs()
import math
import random
from datetime import datetime
import secrets
import numpy as np
#tod: look into numpy array to replace buffer + compare with original code that resizes buffer !!!
from ctypes import CDLL
RAND_MAX=0x7fff
#libc = CDLL(name="libc.so.6")
GA_POPSIZE = 2048  # ga population size
GA_MAXITER = 16384  # // maximum iterations
GA_ELITRATE = 0.10  # // elitism rate
GA_MUTATIONRATE = 0.25  # // mutation rate
GA_MUTATION = RAND_MAX * GA_MUTATIONRATE
GA_TARGET = "Hello world!"
TAR_size=len(GA_TARGET)
#GA_TARGET = "HI !"

""" class for our population has a string and a fitness value"""


class Ga_struct():
    def __init__(self):
        self.string = ""
        self.fitness = 0

    def __lt__(self, other):
        return self.fitness < other.fitness
    def __le__(self, other):
        return self.fitness <= other.fitness
    def __eq__(self, other):
        return self.fitness == other.fitness



""" to generalize the problem we created a class that given a population calculates the solution"""


class genetic_algorithem:
    def __init__(self,target,tar_size,pop_size):
        self.population = list(range(pop_size))
        self.buffer = list(range(pop_size))
        self.target=target
        self.target_size=tar_size
        self.pop_size=pop_size
        self.pop_mean=0
    def init_population(self,pop_size,target_size):
        for i in range(pop_size):
            citizen = Ga_struct()
            for j in range(target_size):
                citizen.string += chr((random.randint(0,90))+32)
            self.population[i]=citizen

# this function calculates fittness for all the population and it's mean value and returns it """

    def calc_fitness(self):


        """mean of all fittness values"""


        mean=0
        for i in range(self.pop_size):
            fitness = 0
            for j in range(self.target_size):
                fit = ord(self.population[i].string[j])-ord(self.target[j])
                fitness += abs(fit)

            self.population[i].fitness = fitness
            # minim=min(minim,fitness)  ## debug purposes
            mean+=fitness
        self.pop_mean=mean/self.pop_size

    def sort_by_fitness(self):
        self.population.sort()

    def elitism(self, esize):
        for i in range(self.pop_size):
            self.buffer[i]=self.population[i]

    def mutate(self,member):
        ipos = random.randint(0, self.target_size-1)
        delta = random.randint(0,90) + 32
        member.string.replace(member.string[ipos], chr((ord(member.string[ipos]) + delta) % 122))

    def mate(self,cross_type):
        esize =  math.floor(self.pop_size * GA_ELITRATE)
        self.elitism(esize)
        self.cross(cross_type)

    def cross(self,cross_type):
        for i in range(self.pop_size):
            i1 = random.randint(0,GA_POPSIZE // 2)
            i2 = random.randint(0,GA_POPSIZE // 2)
            spos = random.randint(0, self.target_size)
            self.buffer[i]=Ga_struct()
            self.buffer[i].string = self.population[i1].string[0:spos] + self.population[i2].string[spos:]
            if (secrets.randbelow(122)< GA_MUTATION):
                self.mutate(self.buffer[i])

    def solve_genetic_problem(self):
        random.seed(datetime.now())
        self.init_population(self.pop_size, self.target_size)
        # for i in self.population:
        #     print(i.string)
        for i in range(GA_MAXITER):

            self.calc_fitness()  # // calculate fitness

            self.sort_by_fitness()

            print_B(self.population)

            print_mean_var((self.pop_mean, variance((self.pop_mean, self.population[0].fitness))))

            if (self.population)[0].fitness == 0: break;

            self.mate(0)  # // mate the population together

            self.population, self.buffer = self.buffer, self.population  # // swap buffers
        return 0

"""inline functions"""


""" that prints the best candidate """
print_B=lambda x:print("Best: " + x[0].string + " (" + str(x[0].fitness) + ")",end=" ")
""" that prints the best candidate """
print_mean_var=lambda x: print("Mean : " + str(x[0]) + " Variance " + str(x[1]))

variance = lambda  x: math.sqrt((x[0]-x[1])**2)

# no need !!!!!


def main():
    GA = genetic_algorithem(GA_TARGET,TAR_size,GA_POPSIZE)
    GA.solve_genetic_problem()
    # t2odo : figure this stuff up libc.srand(unsigned(time(NULL)))
    # random.seed(datetime.now())
    # population, buffer = init_population()
    # for i in population:
    #     print(i.string)
    # for i in range(GA_MAXITER):
    #     mean=calc_fitness(population)  # // calculate fitness
    #     #sort_by_fitness(population)  # // sort them
    #     # print(population[0]<population[1])
    #     sort_by_fitness(population)
    #
    #     print_B(population)
    #
    #     print_mean_var((mean,variance((mean,population[0].fitness))))
    #
    #     if (population)[0].fitness == 0: break;
    #
    #     mate(population, buffer)  # // mate the population together
    #     population, buffer = buffer , population  # // swap buffers
    # return 0

if __name__ == "__main__":
    main()

