import random


# basic class for all problem sets because fittness and the member of the population are problem specific
# and we have to eliminate problem specifc parameters from the Genetic algorithem
# might add mutate !

class parameters:
    def __init__(self):
        self.object = None
        self.fitness = 0


    # creates a member of the population
    def create_object(self,target_size):
        return self.object

    # function to calculate the fitness for this specific problem
    def calculate_fittness(self,target, target_size):
        return self.fitness

    # for sorting purposes
    def __lt__(self, other):
        return self.fitness < other.fitness


# class for first problem
class DNA(parameters):
    def __init__(self):
        parameters.__init__(self)

    def create_object(self,target_size):
        self.object = ""
        for j in range(target_size):
            self.object += chr((random.randint(0, 90)) + 32)
        return self.object

    def calculate_fittness(self,target, target_size):
        for j in range(target_size):
            fit = ord(self.object[j]) - ord(target[j])
            self.fitness += abs(fit)
        return self.fitness
    def mutate(self,target_size,member):
        ipos = random.randint(0,target_size - 1)
        delta = random.randint(0, 90) + 32
        member.object.replace(member.object[ipos], chr((ord(member.object[ipos]) + delta) % 122))



