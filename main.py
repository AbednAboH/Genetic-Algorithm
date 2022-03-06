from settings import *
from Genetic import genetic_algorithem
from PSO import PSO_alg
from create_problem_sets import *
import time
def main():
    fitness_func=int(input("pick fitness"))
    print(fitness_func)
    overall_time = time.perf_counter()
    GA = genetic_algorithem(GA_TARGET, TAR_size, GA_POPSIZE, DNA, 2,fitness_func,2)
    GA.solve()
    # GA = PSO_alg(GA_TARGET, TAR_size, GA_POPSIZE,PSO_prb, fitness_func)
    # GA.solve()
    overall_time = time.perf_counter() - overall_time


if __name__ == "__main__":
    main()