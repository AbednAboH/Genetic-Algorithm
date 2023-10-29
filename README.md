# Genetic Algorithms, PSO, Minimal Conflicts, and First Fit Algorithms

This repository contains implementations of the following algorithms:

1. Genetic Algorithm.
2. Particle Swarm Optimization.
3. Minimal Conflicts.
4. First Fit.

These algorithms are designed to solve a variety of problem sets, including:

1. Bulls and Cows problem.
2. N Queens problem.
3. Bin Packing problem.

The final executable (EXE) file can be found in `dist/main.exe`.

## Requirements:

- Python 3.9 or higher.
- Required libraries: numpy, random, time, math.

**Important Note:** The `main.exe` is located in the `dist` directory. To run it successfully, make sure that the `bin_packing_prob` file is also in the `dist` directory.

**Usage:** Everything can be operated via the command line. To make selections, input the corresponding number and press Enter.

# Console Structure

To configure and execute the program, follow the prompts provided in the console:

1. **Set Population Size:** Input the desired population size.
2. **Choose Algorithm:** Select an algorithm by entering its number (e.g., 1 for GA, 2 for PSO).
3. **Choose Problem to Solve:** Choose a problem to solve by entering the corresponding number (e.g., 1 for Bul Pgia, 2 for N Queens).

## Class Diagram

Here's a simplified diagram of the classes used in this code:

### Parameters for all different algorithms

                        +----------------+                                      +----------------+
                        |   parameters   |                                      |      bin       |
                        +-------+--------+                                      +----------------+
                                ^                                                       ^
                                |                                                       |
                        +----------------+                                      +----------------+ 
                        |      DNA       |                                      | first_fit_prob |        
                        +----------------+                                      +----------------+ 
                               /|\
            +--------+------------+--------------------------+
            |        |            |                          |
       +-------+   +-----------+ +----------------+   +-----------------------+     
       |PSO_prb|   |NQueens_prb| |bin_packing_prob|   |hybrid_bin_packing_prob|
       +-------+   +-----------+ +----------------+   +-----------------------+ 
                                    |
                            +----------------+ 
                            |     bin_pack   |
                            +----------------+ 


### Algorithms


                       
                        +----------------+
                        |   algorithm    |                                              
                        +----------------+                                      
                               /|\
                    +----------+------------+
                    |          |            |                          
               +-------+   +-----------+ +-----------------+    
               |   GA  |   |    PSO    | |Minimal Conflicts|   
               +-------+   +-----------+ +-----------------+ 
                               

# Explanation of the Code Structure

## Introduction

Genetic algorithms (GAs) are a class of evolutionary algorithms. They are population-based optimization techniques inspired by natural selection and genetics. GAs work with a population of potential solutions, using encoding, fitness evaluation, selection, crossover, and mutation to evolve solutions over generations. This code offers a flexible framework for implementing and running genetic algorithm-based solutions across different problem domains, using object-oriented programming to create reusable components.

## Base Class for Problem Parameters
The `parameters` class serves as a base class that can be used for different problem sets. It defines essential attributes and methods that are common across various problem domains:

class parameters:
    def __init__(self):
        self.object = None
        self.fitness = 0

    def create_object(self, target_size):
        # Create an initial object for the population
        return self.object

    def calculate_fitness(self, target, target_size):
        # Calculate fitness based on the chosen fitness function
        self.fitness = self.fitnesstype[select_fitness](self.object, target, target_size)
        return self.fitness

    def __lt__(self, other):
        # For sorting purposes, to allow sorting without lambdas
        return self.fitness < other.fitness

This class defines the parameters for each problem set, allowing customization without altering the genetic algorithm structure.

## Base Class for Genetic Algorithms
The `algorithm` class is a base class for all genetic algorithms and iteration based algorithms that use a population for analytical purposes. It provides core functionality and structure for genetic algorithm solutions:

class algorithm:
    def __init__(self, target, target_size, pop_size, problem_spec, fitnesstype):
        # Initialize algorithm parameters and problem-specific settings

    def init_population(self, pop_size, target_size):
        # Initialize the population based on problem-specific parameters

    def calculate_fitness(self):
        # Calculate fitness according to the selected fitness function

    def sort_by_fitness(self):
        # Sort the population by fitness

    def get_levels_fitness(self):
        # Record fitness for the population in each generation

    def solve(self):
        # Implement the basic structure of the solution for all algorithms
        # Uses the algo(i) function for each generation and a custom stoppage function


## Class for Crossover Functions
The `cross_types` class encapsulates different crossover methods for creating offspring from parent individuals:

Crossing funcitons :
- One Cross.
- Two Cross.
- Uniform Cross.
- CX cross.
- PMX cross.

## Fitness Selector Class
The `fitness_selector` class provides a dictionary of fitness functions, allowing easy selection of the appropriate fitness function for each problem.
including:
- distance fittness.
- Bulls and Cows fitness.

## Mutation Class:
The `mutations` class provides a dictionary of mutation functions ,allowing modular addition and selection of a mutation methode for each problem.
including :
- Random Mutate.
- Swap Mutate.
- Insertion Mutate.
- 
## Selection Methods:
The `slection methods` class provides a dictionary of selection functions, in which the selection of the parents of the new generation of "genes" that are then crossed together and mutated.

including :
- random selection.
- SUS.
- RWS.
- Tornement (Rollete spin selection)
- cross bins


## How It All Fits Together
The code structure allows for modular customization. To use this framework for a specific problem:

1. Define problem-specific parameters by inheriting from the `parameters` class.
2. Create an algorithm class based on the `algorithm` class, adjusting it to the problem's requirements.
3. Select crossover methods, mutation types, and selection methods using the appropriate classes.
4. Implement the `solve` method in your algorithm class to define the solution strategy.

The framework ensures that you can easily adapt the genetic algorithm to various problem domains without altering the core genetic algorithm structure.
