# Ai_lab

## the file Genetic.py contains python code taken from the file given by the teacher of this course 

# updates are done here ! 
	
	* we can now work on the project on python ! 
# updates !

## created a class so that we can use it as a base class for all problem sets to come :
			
			class parameters:
			    def __init__(self):
				self.object = None
				self.fitness = 0


			    # creates a member of the population
			    def create_object(self,target_size):
				return self.object

			    # function to calculate the fitness for this specific problem
			    def calculate_fittness(self,target, target_size):
				return self.fitness

			    # for sorting purposes
			    def __lt__(self, other):
				return self.fitness < other.fitness

* we can now change the above functions for each problem and then just run the algorithem with it , without making changes in the genetic algorithem 
