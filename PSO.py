from algorithems import *

class PSO_alg(algortithem):
    def __init__(self,target, tar_size, pop_size, problem_spec,fitnesstype):
        algortithem.__init__(self,target, tar_size, pop_size, problem_spec,fitnesstype)
        self.glob=problem_spec()
        self.local=problem_spec()

    def calc_fitness(self):
        self.glob.object=self.population[0].object
        self.glob.calculate_fittness(self.target, self.target_size, self.fitnesstype)
        mean = 0
        for i in range(self.pop_size):
            self.population[i].calculate_fittness(self.target, self.target_size, self.fitnesstype)
            if self.population[i].fitness<self.glob.fitness:
                self.glob=self.population[i]

            # names are confusing might get an error
            local=self.prob_spec()
            local.object= self.population[i].best_object
            local.calculate_fittness(self.target,self.target_size,self.fitnesstype)
            if self.population[i].fitness<local.fitness:
                self.population[i].best_object=self.population[i].object

            mean += self.population[i].fitness

        self.pop_mean = mean / self.pop_size
    def algo(self,i):
        self.calc_fitness()
        self.sort_by_fitness()
        w=((i-GA_MAXITER)*0.4)/(GA_MAXITER**2+0.4)
        c1=((-3*i)/GA_MAXITER)+3.5
        c2=((3*i)/GA_MAXITER)+0.5
        for particle in self.population:
            particle.calculate_velocity(c1,c2,self.glob.object,w)
            particle.calculate_new_position()
