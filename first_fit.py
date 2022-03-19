from algorithems import algortithem
from create_problem_sets import bin_packing_prob
from settings import BIN
class FirstFit(algortithem):
    def __init__(self, target, tar_size, problem_spec=None,fitness=None , selection=None):
        super(FirstFit, self).__init__(target, tar_size, 1, problem_spec,BIN , selection)
    def algo(self,i):
        bins=self.prob_spec()
        bins.set_capacity(self.target[1])
        bins.target_creater(self.target)
        bins.create_object(self.target_size,self.target)
        bins.calculate_fittness(self.target, self.target_size, self.fitnesstype)
        self.solution=self.population[0]=bins
    def stopage(self):
        return True