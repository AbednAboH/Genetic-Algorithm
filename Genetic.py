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
#GA_TARGET = "HI !"


class Ga_struct():
    def __init__(self):
        self.string = ""
        self.fitness = 0
        # self.fitness = -1
        # self.fitness = self.fitness + 2 ** 32

    def __lt__(self, other):
        return self.fitness < other.fitness
    def __le__(self, other):
        return self.fitness <= other.fitness
    def __eq__(self, other):
        return self.fitness == other.fitness



def init_population():
    population = []
    buffer = {}
    tsize = len(GA_TARGET)

    for i in range(GA_POPSIZE):
        citizen = Ga_struct()
        for j in range(tsize):
            k= chr((random.randint(0,90))+32)
            citizen.string += k
        population.append(citizen)
        # print(citizen.string)
    # print("---------------------------------------------------------------------------------------")
    return population, buffer


def calc_fitness(population):
    target = GA_TARGET
    tsize = len(target)
    fitness=0
    minim=50000
    for i in range(GA_POPSIZE):
        fitness = 0
        for j in range(tsize):
            fit = ord(population[i].string[j])-ord(target[j])
            fitness += abs(fit)

        population[i].fitness = fitness
        minim=min(minim,fitness)
    print(minim)

def sort_by_fitness(population):
    sorted(population,reverse=True)


def elitism(population, buffer, esize):
    for i in range(esize):
        buffer[i]=population[i]

def mutate(member):
    tsize = len(GA_TARGET)-1
    ipos = random.randint(0, tsize)
    delta = random.randint(0,90) + 32
    # print("ipos",ipos,"     s",member.string)
    member.string.replace(member.string[ipos], chr((ord(member.string[ipos]) + delta) % 122))


def mate(population, buffer):
    esize =  math.floor(GA_POPSIZE * GA_ELITRATE)
    tsize = len(GA_TARGET)
    elitism(population, buffer, esize)
    # print(esize, " ",tsize, " ")

    for i in range(GA_POPSIZE):
        i1 = random.randint(0,GA_POPSIZE // 2)
        i2 = random.randint(0,GA_POPSIZE // 2)
        spos = random.randint(0, tsize)
        buffer[i]=Ga_struct()
        buffer[i].string = population[i1].string[0:spos] + population[i2].string[spos:]
        if (secrets.randbelow(122)< GA_MUTATION):
            mutate(buffer[i])


def print_best(gav):
    print("Best: " + gav[0].string + " (" + str(gav[0].fitness) + ")")


#def swap(population):


# no need !!!!!


def main():
    # t2odo : figure this stuff up libc.srand(unsigned(time(NULL)))
    random.seed(datetime.now())
    population, buffer = init_population()
    for i in population:
        print(i.string)
    for i in range(GA_MAXITER):
        calc_fitness(population)  # // calculate fitness
        #sort_by_fitness(population)  # // sort them
        # print(population[0]<population[1])
        sorted(population)
        print("best",population[0].string)
        print_best(population)  # // print the best one

        if (population)[0].fitness == 0: break;

        mate(population, buffer)  # // mate the population together
        population, buffer = buffer , population  # // swap buffers
    return 0

if __name__ == "__main__":
    main()

