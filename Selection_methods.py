from math import sqrt
import numpy
from random import randint, random, sample
from settings import RAND, SUS, RWS,TOUR


class selection_methods:
    # static propabilies list

    ranks = []

    def __init__(self):
        self.method = {RAND: self.random_selection, SUS: self.SUS, RWS: self.RWS,
                       TOUR: self.tournement}

    def random_selection(self, population, fitness_array, k=10):
        # select random places from half the population
        popsize = len(population)
        i1 = randint(0, popsize // 2)
        i2 = randint(0, popsize // 2)
        return population[i1], population[i2]

    def SUS(self, population, fitness_array, k=10):
        # get comulative sum of all fitness values
        fitness_comulative = fitness_array.cumsum()
        # wheel steps each time we choose
        steps = fitness_comulative[-1] / 2
        # select a random place to begin between 0 and our steps
        begin = random() * steps
        # here we get two evenly spaced places in wheel  !
        new_selection = numpy.arange(begin, fitness_comulative[-1], steps)
        [i1, i2] = numpy.searchsorted(fitness_comulative, new_selection)
        return population[i1], population[i2]

    def RWS(self, population, fitness_array, k=10):
        # check the +1 !
        range_of_choices = len(self.ranks)
        # roll the rullette
        chosen = numpy.random.choice(range_of_choices, p=self.ranks)
        chosen2 = numpy.random.choice(range_of_choices, p=self.ranks)
        return population[chosen], population[chosen2]



    def tournement(self, population, fitness_array, k=25):
        # get samples from population
        participants1 = sample(population, k)
        participants2 = sample(population, k)
        # return minumum from 2 samples
        return min(participants1),min(participants2)

    def spin_the_rulette(self, population, mean):
        # spin the wheel:
        fitness_array = numpy.array([1 / linear_scale((citizen.fitness + 1, 0.5, 0)) for citizen in population])
        fitness_sum = fitness_array.sum()
        self.ranks = [1 / linear_scale((citizen.fitness + 1, 0.5, 0)) / fitness_sum for citizen in population]


def linear_scale(x):
    return x[0] * x[1] + x[2]


# linear_scale = lambda x:x[0]*x[1]+x[2]
e_scale = lambda x: sqrt(x)
