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

class Minimal_conflicts(algortithem):
    def __init__(self, target, tar_size, selection=None):
        algortithem.__init__(self, target, tar_size, 0, NQueens_prb, NQUEENS, selection)
        self.solution.create_object(tar_size)
        # our fitness function that gets a conflict (fitness) value for a specific queen/ position
        self.conflict=self.solution.fitnesstype[3]
    # get conflicts on queens based on there locations and return them as locations with  queen in row ,col  get its number of conflects with others
    def sorted_conflicts(self):
        return [self.conflict(self.solution.object,self.solution.object[i],i ) for i in range(self.target_size)]

    def stopage(self):
        return self.solution.fitness==0
    def select_pos(self,sorted_conflicts):
        return choice([i for i in range(self.target_size) if sorted_conflicts[i]])
    def pos_min(self, sorted_conflicts):
        return choice([i for i in range(self.target_size) if sorted_conflicts[i]==min(sorted_conflicts)])
    def algo(self, i):

        sorted_conflicts=self.sorted_conflicts()
        self.solution.fitness=sum(sorted_conflicts)
        if not self.stopage():
            # get a position that has conflicts by random
            position=self.select_pos(sorted_conflicts)
            # choose based on min conflicts the correct queen
            chosen=self.pos_min([self.conflict(self.solution.object,i,position ) for i in range(self.target_size)])
            # adapt the chosen to the solution
            self.solution.object[position]=chosen
