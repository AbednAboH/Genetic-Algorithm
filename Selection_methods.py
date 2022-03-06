from math import sqrt
import  numpy
from random import randint
from settings import RAND,SUS,RWS,RANK
class selection_methods:

    #static propabilies list

    probabilities = []

    def __init__(self):
        self.method={RAND:self.random_selection,SUS:self.SUS,RWS:self.RWS,RANK:self.Ranking}

    def random_selection(self,population):
        popsize=len(population)
        i1 = randint(0, popsize // 2)
        i2 = randint(0,popsize // 2)
        return i1,i2

    def SUS(self,population):

        pass
    def RWS(self,population):
        # spin the wheel:
        # check the +1 !
        range_of_choices = len(self.probabilities)
        # roll the rullette
        chosen=numpy.random.choice( range_of_choices,p=self.probabilities)
        chosen2=numpy.random.choice( range_of_choices,p=self.probabilities)
        return chosen,chosen2
    def Ranking(self,k):
        pass
    def spin_the_rulette(self,population,mean):
        fitness_array = numpy.array([1 / linear_scale((citizen.fitness + 1, 0.5, 0)) for citizen in population])
        fitness_sum = fitness_array.sum()
        # fitness_sum=mean*len(population)
        # get list of probabilities for which i to choose
        # i = fitness(i)/sum of all fitnesses (all fitnesses are scaled down )
        self.probabilities = [1 / linear_scale((citizen.fitness + 1, 0.5, 0)) / fitness_sum for citizen in population]
        # self.probabilities = [citizen.fitness / fitness_sum for citizen in population]






linear_scale = lambda x:x[0]*x[1]+x[2]
e_scale = lambda x:sqrt(x)