# Ai_lab


## # qualifications:

python 3.9 version

libraries: numpy,random,time,math

* important note : main.exe is in dist file , to run make sure that bin_packing_prob file is in dist 
* everything is in command line 
* to select something press the number next to it then enter , in case of population size,number of queens ; put the number then press enter 


# explenation of the structure of the code 

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
* basically this class defines the parameters for each problem set , as it is expected to change it according to the problem 





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
	    	# here the basic structure of a solution is implemented for all algorithems to come 
		# uses algo(i) where i is the generation number i or the "iteration" 
		# uses stopage() function that stops the code , and is going to be different for each algorithem
	  def algo(self,i):
		here we write the algorithem that we want to implement 
		
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


# implemented classes : 
 
 * the following classes help us to add more functions wothout changing our algorithems , we just have to add the function and give it a key :

* this class gives us a select object that helps us select  the relevant mutate :

	class mutations:

	    def __init__(self):
		self.select = {1: self.random_mutate, 2: self.swap_mutate, 3: self.insertion_mutate, BIN: self.distroy_mutate}

	    def random_mutate(self, target_size, member, character_creation):

	    def swap_mutate(self, target_size, member, character_creation):

	    def insertion_mutate(self, target_size, member, character_creation):


      
* this class does the same thing as the class above but for selections: 


		class selection_methods:
	    # static propabilies list

	    ranks = []

	    def __init__(self):
		self.method = {RAND: self.random_selection, SUS: self.SUS, RWS: self.RWS,
			       TOUR: self.tournement}

	   def random_selection(self, population, fitness_array, k=10):

	   def SUS(self, population, fitness_array, k=10):

	   def RWS(self, population, fitness_array, k=10):

	    def tournement(self, population, fitness_array, k=25):

	    def spin_the_rulette(self, population, mean):
	    
classes for algorithems : 

* the Algorthim class mentioned above gives us basic fanctionality of population ,buffer and more , all the classes of the algorithems are based on it :


* GA:
* algo(self ,i) uses all the new functions in GA class to create a solution and updates the solution and is used in solver() from the father class algorithems
* here we also see how we use cross_types class from above 
* in contrast mutations class is used in a variation of the "citizen/cromosome"  class named parameters , and specifically in DNA class 
* in this way we can create a new hybrid class from this one to make new modifications 

		class genetic_algorithem(algortithem):
		    def __init__(self, target, tar_size, pop_size, problem_spec, crosstype, fitnesstype, selection,
				 serviving_mechanizem,mutation):
			algortithem.__init__(self, target, tar_size, pop_size, problem_spec, fitnesstype, selection)
			self.cross_func = cross_types().select[crosstype]		
			self.serviving = serviving_mechanizem
			self.mutation_type=mutation

		    def mutate(self, member):
			
		    def age_based(self):

		    def mate(self):

		    def cross(self, esize):
		    def algo(self, i):


* DNA class :
* here we see a classic example of using class mutate to spicify the mutation tye based on the object type 

		class DNA(parameters):
		    mutation = mutations()
		    def __init__(self):
			parameters.__init__(self)
		    def create_object(self, target_size, target):
			# for  a specific problem create the right objects 
		    def character_creation(self, target_size):
		    	# create the correct type of character in the cromosome
			return chr((random.randint(0, 90)) + 32)

		    def mutate(self, target_size, member, mutation_type):
			self.mutation.select[mutation_type](target_size, member, self.character_creation)

# pso class created to add more parameters to each cromosome so that pso algorithem can work with it 
			class PSO_prb(DNA):
			    # our object is the initial position , we added 2 parameters that are required
			    def __init__(self):
				DNA.__init__(self)
				self.velocity = None
				self.p_best = sys.maxsize
				self.p_best_object = None

			    def create_special_parameter(self, target_size):
				self.create_velocity(target_size)

			    def create_velocity(self, target_size):
				self.velocity = [random.random() for i in range(target_size)]

			    def calculate_new_position(self):
				pos = ""
				for i in range(len(self.object)):
				    pos += chr((ord(self.object[i]) + int(self.velocity[i])) % 256)
				self.object = pos

			    def calculate_velocity(self, c1, c2, gl_best, w=0.5):
				for i in range(len(self.object)):
				    cc1 = c1 * (ord(self.p_best_object[i]) - ord(self.object[i])) * random.random()
				    cc2 = c2 * (ord(gl_best[i]) - ord(self.object[i])) * random.random()
				    self.velocity[i] = self.velocity[i] * w + cc1 + cc2

			    def __eq__(self, other):
				DNA.__eq__(self, other)
				self.velocity = other.velocity
				self.best_object = other.best_object

			    def __str__(self):
				if self.object == None:
				    return ""
				else:
				    return super(PSO_prb, self).__str__()

## i think that by now the logic is quite clear on how everything fits together 

### so basically , almost every class that has parameters as a forfather is used to change some type of functionality and the gene /cromosome construction of our problem 
* for example :
	* PSO_prb is used for bul pgiaa problem and so has the same structure of a gene in DNA(class for GA in bul pgiaa problem) but with added functionality 
	* but n queens problem is used with the same parameters as bul pgia (called it DNA, should be changed ) but has a different gene/chromosome structure:	
			
			class NQueens_prb(DNA):
			    def __init__(self):
				parameters.__init__(self)
		----->
			    def create_object(self, target_size, target=None):
				obj = random.sample(range(target_size), target_size)
				while len(unique(obj)) != len(obj):
				    obj = random.sample(range(target_size), target_size)
				self.object = obj

			    def character_creation(self, target_size):
		---->		return random.randint(0, target_size - 1)


### and to add an algorithem we just do some modifications on the basic algorithem class :
* for example : Minimal_conflicts :


		class Minimal_conflicts(algortithem):
		    def __init__(self, target, tar_size, selection=None):
			algortithem.__init__(self, target, tar_size, 0, NQueens_prb, NQUEENS, selection)
			self.solution.create_object(tar_size)
			# our fitness function that gets a conflict (fitness) value for a specific queen/ position
			self.conflict = self.solution.fitnesstype[3]

		    # get conflicts on queens based on there locations and return them as locations with  queen in row ,col  get its number of conflects with others
		
		----> changed stopage function
		
		    def stopage(self):
			return self.solution.fitness == 0
		
		----> added functionality :
		
		
		    def sorted_conflicts(self):
			return [self.conflict(self.solution, self.solution.object[i], i) for i in range(self.target_size)]
		    def select_pos(self, sorted_conflicts):
			return choice([i for i in range(self.target_size) if sorted_conflicts[i]])

		    def pos_min(self, sorted_conflicts):
			return choice([i for i in range(self.target_size) if sorted_conflicts[i] == min(sorted_conflicts)])
		
		--->
			changed algo implemetation for this specific function 
		
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
		
