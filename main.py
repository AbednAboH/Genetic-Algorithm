from settings import *
from Genetic import genetic_algorithem
from PSO import PSO_alg
from create_problem_sets import *
import time

algo = {GenA: genetic_algorithem, PSO: PSO_alg}
problem_sets_GA = {BUL_PGIA: DNA}
problem_sets_PSO = {BUL_PGIA: PSO_prb}
elitizem_or_aging={}

def main():
    alg = int(input("chose algorithem :  1:GA  2:PSO"))
    solution=None
    if alg == GenA:
        problem_set = problem_sets_GA[int(input("choose problem to solve :  1:Bul Pgia "))]
        fit=int(input("choose fitness function :  0:Distance  1:Bul Pgia "))
        crosstype=int(input("choose cross function :  One Cross: 1  Two Cross: 2  Uniform: 3"))
        selection=int(input("choose selection function :  RAND: 0  SUS: 1  RWS: 2  RANK:3"))
        serviving_stratigy=int(input("choose surviving strategy :  Elite: 1 ,Age: 2"))

        solution=algo[alg](GA_TARGET,TAR_size,GA_POPSIZE,problem_set,crosstype,fit,selection,serviving_stratigy)
    elif alg == PSO:
        problem_set = problem_sets_PSO[int(input("choose problem to solve :  1:Bul Pgia "))]
        fit = int(input("choose fitness function :  0:Distance  1:Bul Pgia "))
        solution=algo[alg](GA_TARGET,TAR_size,GA_POPSIZE,problem_set,fit)

    overall_time = time.perf_counter()
    solution.solve()
    overall_time = time.perf_counter() - overall_time


if __name__ == "__main__":
    main()
