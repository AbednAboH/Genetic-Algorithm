import random
PENALTY=30
HIGH_PENALTY=100

class fitness_selector:
    def __init__(self):
        self.select={0:self.distance_fittness,1:self.bul_pqia}

    def distance_fittness(self,object, target, target_size):
        fitness=0
        for j in range(target_size):
            fit = ord(object[j]) - ord(target[j])
            fitness += abs(fit)
        return fitness

    def bul_pqia(self,object, target, target_size):
        fitness=0
        for i in range(target_size):
            if object[i]!=target[i]:
                fitness += PENALTY if object[i] in target else HIGH_PENALTY
        return fitness
    ## fitness for pso
# basic class for all problem sets because fittness and the member of the population are problem specific
# and we have to eliminate problem specifc parameters from the Genetic algorithem
# might add mutate !
class parameters:
    def __init__(self):
        self.fitnesstype=fitness_selector().select
        self.object = None
        self.fitness = 0

    # creates a member of the population
    def create_object(self,target_size):
        return self.object

    # function to calculate the fitness for this specific problem
    def calculate_fittness(self,target, target_size,select_fitness):
        self.fitness=self.fitnesstype[select_fitness](self.object,target,target_size)
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

    def mutate(self,target_size,member):
        ipos = random.randint(0,target_size - 1)
        delta = random.randint(0, 90) + 32
        # can be written differently ,i.e more general
        member.object.replace(member.object[ipos], chr((ord(member.object[ipos]) + delta) % 122))

# class for pso problem

