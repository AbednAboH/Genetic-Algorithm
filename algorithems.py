import math
import time
from Selection_methods import selection_methods
from settings import GA_MAXITER
import numpy


class algortithem:
    def __init__(self, target, tar_size, pop_size, problem_spec, fitnesstype, selection):
        self.population = list(range(pop_size))
        self.buffer = list(range(pop_size))
        self.fitness_array = numpy.zeros((pop_size))
        self.target = target
        self.target_size = tar_size
        self.pop_size = pop_size
        self.pop_mean = 0
        self.iteration = 0  # current iteration that went through the algorithem
        self.prob_spec = problem_spec
        self.file = open(r"pres.txt", "w+")
        self.fitnesstype = fitnesstype
        self.selection_methods = selection_methods()
        self.selection = selection
        self.tick = 0
        self.sol_time = 0
        self.solution = problem_spec()

    def init_population(self):
        for i in range(self.pop_size):
            citizen = self.prob_spec()
            citizen.create_object(self.target_size)
            citizen.calculate_fittness(self.target, self.target_size, self.fitnesstype)
            self.population[i] = self.buffer[i] = citizen
            self.fitness_array[i] = (1 / citizen.fitness+1)
        self.sort_by_fitness()

    def calc_fitness(self):
        mean = 0
        for i in range(self.pop_size):
            self.population[i].calculate_fittness(self.target, self.target_size, self.fitnesstype)
            # mean += self.population[i].fitness
        for i in range(self.pop_size):
            mean += self.population[i].fitness

        self.pop_mean = mean / self.pop_size

    def sort_by_fitness(self):
        self.population = sorted(self.population)

    def update_fitness_array(self):
        for j in range(self.pop_size):
            self.fitness_array[j] = 1 / (self.population[j].fitness+1)

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
        print_B(self.solution)
        print_mean_var((self.pop_mean, variance((self.pop_mean, self.population[0].fitness))))
        print_time((runtime, clockticks))

    def algo(self, i):
        pass

    def stopage(self):
        return self.population[0].fitness == 0

    def solve(self):
        self.handle_initial_time()
        self.init_population()
        for i in range(GA_MAXITER):
            # self.file.write("i" + str(self.iteration) + "\n")

            self.iteration += 1

            self.algo(i)

            self.get_levels_fitness()

            self.handle_prints_time()

            if self.stopage():
                break

        # self.file.close()
        return 0


print_B = lambda x: print(f" Best: ,fittness: {x.fitness} ", end=" ")
# print_B = lambda x: print(f" Best: {x.object} ,fittness: {x.fitness} ", end=" ")

#  prints mean and variance
print_mean_var = lambda x: print(f"Mean: {x[0]} ,Variance: {x[1]}", end=" ")
# prints time
print_time = lambda x: print(f"Time :  {x[0]}  ticks: {x[1]}")
# calculates variance
variance = lambda x: math.sqrt((x[0] - x[1]) ** 2)
