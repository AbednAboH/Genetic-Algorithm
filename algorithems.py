import math
import random
import secrets
import time

RAND_MAX = 0x7fff

GA_POPSIZE = 2048
GA_MAXITER = 16384
GA_ELITRATE = 0.10
GA_MUTATIONRATE = 0.25
GA_MUTATION = RAND_MAX * GA_MUTATIONRATE
GA_TARGET = "you are my sunshine!"
TAR_size = len(GA_TARGET)


class algortithem:
    def __init__(self, target, tar_size, pop_size, problem_spec,fitnesstype):
        self.population = list(range(pop_size))
        self.buffer = list(range(pop_size))
        self.target = target
        self.target_size = tar_size
        self.pop_size = pop_size
        self.pop_mean = 0
        self.iteration = 0  # current iteration that went through the algorithem
        self.prob_spec = problem_spec
        self.file = open(r"pres.txt", "w+")
        self.fitnesstype=fitnesstype
        self.tick=0
        self.sol_time=0

    def init_population(self, pop_size, target_size):
        for i in range(pop_size):
            citizen = self.prob_spec()
            citizen.create_object(target_size)
            citizen.calculate_fittness(self.target, target_size, self.fitnesstype)
            self.population[i] = citizen
    def calc_fitness(self):
        mean = 0
        for i in range(self.pop_size):
            self.population[i].calculate_fittness(self.target, self.target_size,self.fitnesstype)
            mean += self.population[i].fitness

        self.pop_mean = mean / self.pop_size

    def sort_by_fitness(self):
        self.population.sort()

    def get_levels_fitness(self):
        arr = {}
        for i in self.population:
            if i.fitness in arr.keys():
                arr[i.fitness] += 1
            else:
                arr[i.fitness] = 1
        for i in arr.keys():
            self.file.write(str(i) + " " + str(arr[i]) + "\n")

    def handle_initial_time(self):
        self.tick = time.time()
        self.sol_time = time.perf_counter()

    def handle_prints_time(self):
        runtime = time.perf_counter() - self.sol_time
        clockticks = time.time() - self.tick
        print_B(self.population)
        print_mean_var((self.pop_mean, variance((self.pop_mean, self.population[0].fitness))))
        print_time((runtime, clockticks))

    def algo(self,i):
        pass

    def solve(self):
        self.handle_initial_time()
        self.init_population(self.pop_size, self.target_size)
        for i in self.population:
            print(i.object)
        for i in range(GA_MAXITER):
            self.file.write("i" + str(self.iteration) + "\n")

            self.iteration += 1

            self.algo(i)
            self.get_levels_fitness()
            self.handle_prints_time()
            if (self.population)[0].fitness == 0: break


        self.file.close()
        return 0

print_B = lambda x: print(f" Best: {x[0].object} ,fittness: {x[0].fitness} ", end=" ")

#  prints mean and variance
print_mean_var = lambda x: print(f"Mean: {x[0]} ,Variance: {x[1]}", end=" ")
# prints time
print_time = lambda x: print(f"Time :  {x[0]}  ticks: {x[1]}")
# calculates variance
variance = lambda x: math.sqrt((x[0] - x[1]) ** 2)