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



## added class for cross function :

	class cross_types:

	    def __init__(self):
		# maps functions to numbers so that we can choose which one to assign
		self.select = {1: self.one_cross, 2: self.two_cross, 3: self.uniform_cross}

	    def one_cross(self, citizen1, citizen2):
		target_size = len(citizen1)
		spos = random.randint(0, target_size)
		return citizen1[0:spos] + citizen2[spos:target_size], citizen2[0:spos] + citizen1[spos:target_size]

	    def two_cross(self, citizen1, citizen2):
		target_size = len(citizen1)
		spos = random.randint(0, target_size - 2)  # we need at least 3 portions
		spos2 = random.randint(spos, target_size - 1)  # we need at least 2 portions
		first = citizen1[0:spos] + citizen2[spos:spos2] + citizen1[spos2 :]
		sec = citizen2[0:spos] + citizen1[spos:spos2] + citizen2[spos2:]
		return first, sec

	    def uniform_cross(self, citizen1, citizen2):
		target_size = len(citizen1)
		object1 = []
		object2 = []
		for i in range(target_size):
		    if random.random() > 0.5:
			object1.append(citizen2[i])
			object2.append(citizen1[i])
		    else:
			object1.append(citizen1[i])
			object2.append(citizen2[i])
		return object1, object2

