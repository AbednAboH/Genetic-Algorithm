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

			    # function to calculate the given fitness function for this problem 
			    def calculate_fittness(self,target, target_size):
				self.fitness=self.fitnesstype[select_fitness](self.object,target,target_size)
       				 return self.fitness

			    # for sorting purposes so that sort or sorted can be used without lambda's 
			    def __lt__(self, other):
				return self.fitness < other.fitness

* we can now change the above functions for each problem and then just run the algorithem with it , without making changes in the genetic algorithem 



## added class for cross function :
	
	class cross_types:
	all of the functions below return 2 objects in the format of the problem
	    def __init__(self):
		# maps functions to numbers so that we can choose which one to assign
		self.select = {1: self.one_cross, 2: self.two_cross, 3: self.uniform_cross}

	    def one_cross(self, citizen1, citizen2):
		return citizen1[0:spos] + citizen2[spos:target_size], citizen2[0:spos] + citizen1[spos:target_size]

	    def two_cross(self, citizen1, citizen2):
		return first, sec

	    def uniform_cross(self, citizen1, citizen2):
		return object1, object2


## base class for all algorithems :

	class algortithem:
	    def __init__(self, target, tar_size, pop_size, problem_spec,fitnesstype):

	    def init_population(self, pop_size, target_size):
		# initiates population based on the problem_spec (problem specific) parameters 
	    def calc_fitness(self):
		# calculates fitness accorrding to fitness type 

	    def sort_by_fitness(self):
		# sorts population by fitness ,static for all algorithems
		
	    def get_levels_fitness(self):
		# writes fitness for the population in each generation 

	    def solve(self):
	    	# here the algorithem is implemented for each algorithem 
		# might add a seperate function that handls time 
		
## fitness selector class has a dictionary with all fitness functions so that we can choose the one that we want when we use calculate fitness 
	class fitness_selector:
	    def __init__(self):
		self.select={0:self.distance_fittness,1:self.bul_pqia}

	    def distance_fittness(self,object, target, target_size):
		fitness=0
		for j in range(target_size):
		    fit = ord(object[j]) - ord(target[j])
		    fitness += abs(fit)
		return fitness

	    def bul_pqia(self,object, target, target_size):
		fitness=0
		for i in range(target_size):
		    if object[i]!=target[i]:
			fitness += PENALTY if object[i] in target else HIGH_PENALTY
		return fitness
		
# how it all fits together 

* we define how we get the population using a new class that has a base class parameters and apply changes to it 
	* create object function , creates a citizen in the population 
	* calculate fitness uses the class fitness_selector to take the appropriate function from it 
* we define an algoritem using an algorithem class that creates the population based on the problem above ,
	* in other words given a class of problems ,algorithem class creates all relevant fields based on the problem specific class , i.e creates population and calculates fitness based on it 

### by now we have all the tools that we need ,and the rest is history :P + make a way to select the mutaions , another tiny class would safice 



