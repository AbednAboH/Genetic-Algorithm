# class for fitness functions , add your fitness function here !
from settings import BIN,HIGH_PENALTY,PENALTY
from numpy import unique
from math import ceil
hash_table = {}
class fitness_selector:
    def __init__(self):
        self.select = {0: self.distance_fittness, 1: self.bul_pqia, 2: self.n_queens_conflict,
                       3: self.n_queens_conf_based_on_place, BIN: self.bins_fitness}

    def distance_fittness(self, object, target, target_size):
        fitness = 0
        for j in range(target_size):
            fit = ord(object.object[j]) - ord(target[j])
            fitness += abs(fit)
        return fitness

    def bul_pqia(self, object, target, target_size):
        fitness = 0
        for i in range(target_size):
            if ord(object.object[i]) != ord(target[i]):
                fitness += PENALTY if object.object[i] in target else HIGH_PENALTY
        return fitness

    # fitness for NQueens:
    def n_queens_conflict(self, object, target, target_size):
        conflicts = 0
        for col in range(target_size):
            for row in range(target_size):
                if row != col:
                    # check if more than one queen is on the same right diagonal "/"
                    conflicts += 1 if abs(row - col) == abs(object.object[col] - object.object[row]) else 0
        # check for duplicates ! ,cannot be detected by diagonal's
        conflicts += abs(len(unique(object.object)) - len(object.object))

        return conflicts

    def n_queens_conf_based_on_place(self, object, row, col):
        conflicts = 0
        for i in range(len(object.object)):
            if i == col:
                continue
            if (object.object[i] == row or abs(object.object[i] - row) == abs(i - col)):
                conflicts += 1
        return conflicts

    def bins_fitness(self, object, target, target_size):

        object.create_special_parameter(target_size)
        capacity = object.bin_objects[0].capacity
        sumof = sum([hash_table[i] for i in object.object]) / capacity

        number_of_bins = len(object.bin_objects)
        return abs(ceil(sumof*9/8)-number_of_bins)

    ## fitness for pso

