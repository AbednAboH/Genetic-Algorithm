from create_problem_sets import *
from function_selection import cross_types
from algorithems import *
from PSO import *
""" to generalize the problem we created a class that given a population calculates the solution"""



class genetic_algorithem(algortithem):
    def __init__(self, target, tar_size, pop_size, problem_spec, crosstype,fitnesstype):
        algortithem.__init__(self,target, tar_size, pop_size, problem_spec,fitnesstype)
        self.cross_func = cross_types().select[crosstype]

    # this function calculates fittness for all the population and it's mean value and returns it """

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
            citizen1.object, citizen2.object = self.cross_func(self.population[i1].object, self.population[i2].object)
            citizen1.calculate_fittness(self.target,self.target_size,self.fitnesstype)
            citizen2.calculate_fittness(self.target,self.target_size,self.fitnesstype)
            # select best of the two
            self.buffer[i]=citizen1 if citizen1.fitness<citizen2.fitness else citizen2

            if (secrets.randbelow(122) < GA_MUTATION):
                self.mutate(self.buffer[i])
    def algo(self,i):
        self.calc_fitness()  # // calculate fitness

        self.sort_by_fitness()
        self.mate()  # // mate the population together

        self.population, self.buffer = self.buffer, self.population  # // swap buffers




# inline functions


# that prints the best candidate




# no need !!!!!


def main():
    fitness_func=int(input("pick fitness"))
    print(fitness_func)
    overall_time = time.perf_counter()
    # GA = genetic_algorithem(GA_TARGET, TAR_size, GA_POPSIZE, DNA, 2,fitness_func)
    # GA.solve()
    GA = PSO_alg(GA_TARGET, TAR_size, GA_POPSIZE,PSO_prb, fitness_func)
    GA.solve()
    overall_time = time.perf_counter() - overall_time


if __name__ == "__main__":
    main()
