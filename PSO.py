from algorithems import *
from settings import GA_MAXITER,NQUEENS
from random import choice
from create_problem_sets import NQueens_prb

class PSO_alg(algortithem):
    def __init__(self, target, tar_size, pop_size, problem_spec, fitnesstype, selection=None):
        algortithem.__init__(self, target, tar_size, pop_size, problem_spec, fitnesstype, selection)
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

            if particle.fitness < particle.p_best:
                particle.p_best = particle.fitness
                particle.p_best_object = particle.object

            mean += particle.fitness
        self.pop_mean = mean / self.pop_size

    def algo(self, i):
        if i == 0:
            self.global_minima.object = self.population[0].object
            self.global_minima.calculate_fittness(self.target, self.target_size, self.fitnesstype)
        self.calc_fitness()
        self.sort_by_fitness()

        w = ((i - GA_MAXITER) * 0.4) / (GA_MAXITER ** 2 + 0.4)
        c1 = ((-3 * i) / GA_MAXITER) + 2
        c2 = ((3 * i) / GA_MAXITER) + 2
        if not self.stopage():
            for particle in self.population:
                particle.calculate_velocity(c1, c2, self.global_minima.object, w)
                particle.calculate_new_position()

    def stopage(self):
        return self.global_minima.fitness == 0


