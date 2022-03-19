from algorithems import algortithem
from settings import NQUEENS
from create_problem_sets import NQueens_prb
from random import choice
class Minimal_conflicts(algortithem):
    def __init__(self, target, tar_size, selection=None):
        algortithem.__init__(self, target, tar_size, 0, NQueens_prb, NQUEENS, selection)
        self.solution.create_object(tar_size)
        # our fitness function that gets a conflict (fitness) value for a specific queen/ position
        self.conflict = self.solution.fitnesstype[3]

    # get conflicts on queens based on there locations and return them as locations with  queen in row ,col  get its number of conflects with others
    def sorted_conflicts(self):
        return [self.conflict(self.solution, self.solution.object[i], i) for i in range(self.target_size)]

    def stopage(self):
        return self.solution.fitness == 0

    def select_pos(self, sorted_conflicts):
        return choice([i for i in range(self.target_size) if sorted_conflicts[i]])

    def pos_min(self, sorted_conflicts):
        return choice([i for i in range(self.target_size) if sorted_conflicts[i] == min(sorted_conflicts)])

    def algo(self, i):
        sorted_conflicts = self.sorted_conflicts()
        self.solution.fitness = sum(sorted_conflicts)
        if not self.stopage():
            # get a position that has conflicts by random
            position = self.select_pos(sorted_conflicts)
            # choose based on min conflicts the correct queen
            chosen = self.pos_min([self.conflict(self.solution, i, position) for i in range(self.target_size)])
            # adapt the chosen to the solution
            self.solution.object[position] = chosen
