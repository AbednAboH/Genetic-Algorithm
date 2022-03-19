from settings import *
from Genetic import genetic_algorithem
from PSO import PSO_alg
from Minimal_conflicts import  Minimal_conflicts
from first_fit import FirstFit
from create_problem_sets import *
import time

algo = {GenA: genetic_algorithem, PSO: PSO_alg, MINIMAL_CONF: Minimal_conflicts ,FIRST_FIT:FirstFit}
problem_sets_GA = {BUL_PGIA: DNA, NQUEENS: NQueens_prb, 3: bin_packing_prob}
problem_sets_PSO = {BUL_PGIA: PSO_prb}
problem_sets_bin_packing = {1:'N1C1W1_A',2:'N1C1W1_B',3:'N1C1W1_C',4:'N1C1W1_D'}

def get_bin_packing_weights(name):
    file = open(fr"bin_packing_prob\{name}.BPP", "r")
    weights=file.read().splitlines()
    weights1=[int(k) for k in weights]
    file.close()
    return weights1[0],weights1[1],weights1[2:]
def main():
    alg = int(input("chose algorithem :  1:GA  2:PSO 3:Minimal conflicts"))
    solution = None
    if alg == GenA:
        prob = int(input("choose problem to solve :  1:Bul Pgia  2:N Queens 3:Bin Packing Prob"))
        problem_set = problem_sets_GA[prob]

        serviving_stratigy = int(input("choose surviving strategy :  Elite: 1 ,Age: 2"))
        if prob == BUL_PGIA:
            crosstype = int(input("choose cross function :  One Cross: 1  Two Cross: 2  Uniform: 3  PMX: 4   CX: 5"))
            selection = int(input("choose selection function :  RAND: 0  SUS: 1  RWS: 2  RANK:3"))
            fit = int(input("choose fitness function :  0:Distance  1:Bul Pgia   "))
            mutation = int(input("choose mutation scheme:  random mutation: 1 ,swap_mutate: 2 ,insertion_mutate: 3"))
            target_size = TAR_size
        elif prob == NQUEENS:
            fit = NQUEENS
            crosstype = int(input("choose cross function :  One Cross: 1  Two Cross: 2  Uniform: 3  PMX: 4   CX: 5"))
            selection = int(input("choose selection function :  RAND: 0  SUS: 1  RWS: 2  RANK:3"))
            mutation = int(input("choose mutation scheme:swap_mutate: 2 ,insertion_mutate: 3"))
            target_size = int(input("choose number of queens :"))
        else:# bin_packing

            target=[]
            selection = int(input("choose selection function :  RAND: 0  SUS: 1  RWS: 2  RANK:3"))
            # get problem weights from file
            bin_pack_prob=int(input("N1C1W1_A: 1 ,N1C1W1_B: 2,N1C1W1_C: 3,N1C1W1_D: 4"))
            # send target with [real target with numbers instead of weights,capacity of each bin]
            n,capacity,weights=get_bin_packing_weights(problem_sets_bin_packing[bin_pack_prob])
            target.append([i for i in range(len(weights))])
            target.append(int(capacity))
            # print(target[0])
            # give hash table correct keys so that everything works !
            for i in range(len(target[0])):
                hash_table[i] = weights[i]
            print(hash_table)

            # add target to problem
            problem_set.target=target
            problem_set.capacity=target[1]
            fit=BIN
            crosstype = int(input("choose cross function :  One Cross: 1  Two Cross: 2  Uniform: 3  PMX: 4   CX: 5"))
            mutation = int(input("choose mutation scheme:  random mutation: 1 ,swap_mutate: 2 ,insertion_mutate: 3"))
            target_size=10
        solution = algo[alg](GA_TARGET, target_size, GA_POPSIZE, problem_set, crosstype, fit, selection,
                             serviving_stratigy, mutation)
    elif alg == PSO:
        problem_set = problem_sets_PSO[int(input("choose problem to solve :  1:Bul Pgia "))]
        fit = int(input("choose fitness function :  0:Distance  1:Bul Pgia "))
        solution = algo[alg](GA_TARGET, TAR_size, GA_POPSIZE, problem_set, fit)
    elif alg == MINIMAL_CONF:
        target_size = int(input("choose number of queens :"))
        target = None
        solution = algo[alg](target, target_size, selection=None)

        overall_time = time.perf_counter()
    elif alg==FIRST_FIT:
        problem_set = problem_sets_GA[3]
        target = []
        # get problem weights from file
        bin_pack_prob = int(input("N1C1W1_A: 1 ,N1C1W1_B: 2,N1C1W1_C: 3,N1C1W1_D: 4"))
        # send target with [real target with numbers instead of weights,capacity of each bin]
        n, capacity, weights = get_bin_packing_weights(problem_sets_bin_packing[bin_pack_prob])
        target.append([i for i in range(len(weights))])
        target.append(int(capacity))
        for i in range(len(target[0])):
            hash_table[i] = weights[i]
        print(hash_table)
        # add target to problem
        problem_set.target = target
        problem_set.capacity = target[1]
        solution = algo[alg](target, capacity,problem_set)
    overall_time = time.perf_counter()
    solution.solve()
    overall_time = time.perf_counter() - overall_time
    print("Overall runtime :",overall_time)

if __name__ == "__main__":
    main()
