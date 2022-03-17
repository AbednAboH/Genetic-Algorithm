from settings import *
from Genetic import genetic_algorithem
from PSO import PSO_alg
from create_problem_sets import *
import time

algo = {GenA: genetic_algorithem, PSO: PSO_alg}
problem_sets_GA = {BUL_PGIA: DNA, NQUEENS: NQueens_prb}
problem_sets_PSO = {BUL_PGIA: PSO_prb}
elitizem_or_aging = {}


def main():
    alg = int(input("chose algorithem :  1:GA  2:PSO"))
    solution = None
    if alg == GenA:
        prob = int(input("choose problem to solve :  1:Bul Pgia  2:N Queens "))
        problem_set = problem_sets_GA[prob]
        crosstype = int(input("choose cross function :  One Cross: 1  Two Cross: 2  Uniform: 3  PMX: 4   CX: 5"))
        selection = int(input("choose selection function :  RAND: 0  SUS: 1  RWS: 2  RANK:3"))
        serviving_stratigy = int(input("choose surviving strategy :  Elite: 1 ,Age: 2"))
        if prob == BUL_PGIA:
            fit = int(input("choose fitness function :  0:Distance  1:Bul Pgia   "))
            mutation = int(input("choose mutation scheme:  random mutation: 1 ,swap_mutate: 2 ,insertion_mutate: 3"))
            target_size = TAR_size
        else:
            fit = NQUEENS
            mutation = int(input("choose mutation scheme:swap_mutate: 2 ,insertion_mutate: 3"))
            target_size = int(input("choose number of queens :"))
        solution = algo[alg](GA_TARGET, target_size, GA_POPSIZE, problem_set, crosstype, fit, selection,
                             serviving_stratigy,mutation)
    elif alg == PSO:
        problem_set = problem_sets_PSO[int(input("choose problem to solve :  1:Bul Pgia "))]
        fit = int(input("choose fitness function :  0:Distance  1:Bul Pgia "))
        solution = algo[alg](GA_TARGET, TAR_size, GA_POPSIZE, problem_set, fit)

    overall_time = time.perf_counter()

    solution.solve()
    overall_time = time.perf_counter() - overall_time


if __name__ == "__main__":
    main()
