from algorithems import *
from settings import GA_MAXITER

class PSO_alg(algortithem):
    def __init__(self, target, tar_size, pop_size, problem_spec, fitnesstype):
        algortithem.__init__(self, target, tar_size, pop_size, problem_spec, fitnesstype)
        self.global_minima = problem_spec()
        self.local_minima = problem_spec()

    def calc_fitness(self):

        mean = 0
        for particle in self.population:

            particle.calculate_fittness(self.target, self.target_size, self.fitnesstype)

            local_minima = self.prob_spec()

            if particle.fitness == 0:
                self.solution = self.global_minima = particle
                break
            if particle.fitness < self.global_minima.fitness:
                self.solution = self.global_minima = particle


            local_minima.object = particle.best_object
            local_minima.calculate_fittness(self.target, self.target_size, self.fitnesstype)

            if particle.fitness < local_minima.fitness:
                particle.best_object = particle.object

            mean += particle.fitness
        self.pop_mean = mean / self.pop_size

    def algo(self, i):
        if i == 0:
            self.global_minima.object = self.population[0].object
            self.global_minima.calculate_fittness(self.target, self.target_size, self.fitnesstype)
        self.calc_fitness()

        w = ((i - GA_MAXITER) * 0.4) / (GA_MAXITER ** 2 + 0.4)
        c1 = ((-3 * i) / GA_MAXITER) + 3.5
        c2 = ((3 * i) / GA_MAXITER) + 0.5
        if not self.stopage():
            for particle in self.population:
                particle.calculate_velocity(c1, c2, self.global_minima.object, w)
                particle.calculate_new_position()

    def stopage(self):
        return self.global_minima.fitness == 0
