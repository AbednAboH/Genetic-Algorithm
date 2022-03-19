from create_problem_sets import *
from function_selection import cross_types
from PSO import *
from settings import *
from sys import maxsize

""" to generalize the problem we created a class that given a population calculates the solution"""


class genetic_algorithem(algortithem):
    def __init__(self, target, tar_size, pop_size, problem_spec, crosstype, fitnesstype, selection,
                 serviving_mechanizem,mutation):
        algortithem.__init__(self, target, tar_size, pop_size, problem_spec, fitnesstype, selection)
        self.cross_func = cross_types().select[crosstype]
        self.serviving = serviving_mechanizem
        self.mutation_type=mutation

    # this function calculates fittness for all the population and it's mean value and returns it """



    def mutate(self, member):
        member.mutate(self.target_size, member,self.mutation_type)

    def age_based(self):
        age_based_population = [citizen for citizen in self.population if 2 <= citizen.age <= 20]
        self.buffer[:len(age_based_population)] = age_based_population[:]
        return len(age_based_population)

    def mate(self):
        #elitizem
        esize = math.floor(self.pop_size * GA_ELITRATE)
        if self.serviving == ELITIZEM:
            self.buffer[:esize] = self.population[:esize]
        #age
        elif self.serviving == AGE:
            esize = self.age_based()

        self.cross(esize)

    def cross(self, esize):
        ### maybe population needs to go down ! so use buffer.append ! maybe not sure !
        if self.selection == RWS:
            self.selection_methods.spin_the_rulette(self.population, self.pop_mean)
        for i in range(esize, self.pop_size):
            self.buffer[i] = self.prob_spec()
            citizen1 = self.prob_spec()
            citizen2 = self.prob_spec()
            i1, i2 = self.selection_methods.method[self.selection](self.population, self.fitness_array)
            citizen1.object, citizen2.object = self.cross_func(i1, i2)
            citizen1.calculate_fittness(self.target, self.target_size, self.fitnesstype)
            citizen2.calculate_fittness(self.target, self.target_size, self.fitnesstype)
            # select best of the two
            self.buffer[i] = citizen1 if citizen1.fitness < citizen2.fitness else citizen2

            if (random.randint(0, maxsize) < GA_MUTATION):
                self.mutate(self.buffer[i])

    def algo(self, i):
        self.calc_fitness()  # // calculate fitness
        self.sort_by_fitness()
        self.update_fitness_array()
        self.mate()  # // mate the population together

        self.population, self.buffer = self.buffer, self.population  # // swap buffers
        self.solution = self.population[0]

# inline functions


# that prints the best candidate


# no need !!!!!
