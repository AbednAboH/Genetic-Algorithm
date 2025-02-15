# Genetic Algorithm and Optimization Techniques

## Overview
This repository contains Python implementations of various optimization algorithms designed to tackle complex problems. The primary algorithms included are:

- **Genetic Algorithm (GA)**: An evolutionary algorithm inspired by natural selection.
- **Particle Swarm Optimization (PSO)**: A population-based optimization technique inspired by the social behavior of birds and fish.
- **Minimal Conflicts Algorithm**: A heuristic-based local search for constraint satisfaction problems.
- **First Fit Algorithm**: A greedy approach to the bin packing problem.

## Problem Domains Addressed
The algorithms are applied to solve the following problems:

- **Bulls and Cows Problem**: A code-breaking game where the objective is to guess a secret code based on feedback.
- **N Queens Problem**: Placing N chess queens on an N×N board so that no two queens threaten each other.
- **Bin Packing Problem**: Efficiently packing objects of different volumes into a finite number of bins with fixed capacity.

---

## Project Structure
```
Genetic-Algorithm/
│── Genetic.py              # Implementation of Genetic Algorithm
│── PSO.py                  # Implementation of Particle Swarm Optimization
│── Minimal_conflicts.py     # Implementation of Minimal Conflicts Algorithm
│── first_fit.py             # Implementation of First Fit Algorithm
│── main.py                  # Entry point to run the selected algorithm
│── fitness_functions.py     # Defines problem-specific fitness evaluation methods
│── Selection_methods.py     # Various selection strategies for GA
│── mutations.py             # Mutation strategies for GA
│── create_problem_sets.py   # Functions to generate problem instances
│── settings.py              # Configurations for running experiments
│── README.md                # Documentation file (this file)
│── requirements.txt         # List of required Python libraries
│── setup.py                 # Installation setup file
└── utils/                   # Contains helper functions for various computations
```

---

## Installation & Setup

### Prerequisites
- Python 3.x
- Required Python libraries (see `requirements.txt`)

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AbednAboH/Genetic-Algorithm.git
   cd Genetic-Algorithm
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` is missing, manually install dependencies such as NumPy:
   ```bash
   pip install numpy
   ```

---

## Usage Guide

### Configuring the Algorithm
Before running an algorithm, configure the **`settings.py`** file to select:

- The algorithm to use (`GA`, `PSO`, `Minimal Conflicts`, or `First Fit`).
- The problem to solve (`Bulls and Cows`, `N Queens`, or `Bin Packing`).
- The hyperparameters, such as population size, mutation rate, and number of generations.

### Running the Algorithm
Once configured, run the script:
```bash
python main.py
```
This will execute the selected optimization algorithm with the specified problem and settings.

### Example: Running the Genetic Algorithm
If `settings.py` is configured to use the Genetic Algorithm for the N-Queens problem, running:
```bash
python main.py
```
will execute the algorithm and output the results.

---

## Algorithm Implementations

### 1. Genetic Algorithm (GA)
- **Concept**: Evolutionary search that mimics natural selection.
- **Key Components**:
  - **Selection Methods** (e.g., Tournament Selection, Roulette Wheel)
  - **Crossover Operators** (e.g., One-Point, Two-Point, Uniform)
  - **Mutation Techniques** (e.g., Random Bit Flip, Swap Mutation)
- **Customization**: Users can modify `Selection_methods.py` and `mutations.py` to experiment with different approaches.

### 2. Particle Swarm Optimization (PSO)
- **Concept**: Optimization based on the movement and intelligence of particle swarms.
- **Key Components**:
  - Particle Position & Velocity Updates
  - Personal and Global Best Tracking
- **Customization**: Modify `PSO.py` to adjust swarm size and update equations.

### 3. Minimal Conflicts Algorithm
- **Concept**: A heuristic-based method for solving constraint satisfaction problems.
- **Key Use Case**: The N-Queens problem.
- **Customization**: Modify `Minimal_conflicts.py` to add heuristics for different CSPs.

### 4. First Fit Algorithm
- **Concept**: A greedy algorithm for packing items efficiently.
- **Key Use Case**: Bin Packing problem.
- **Customization**: Modify `first_fit.py` for alternative packing strategies.

---

## How to Extend the Project

### Adding a New Algorithm
1. Create a new Python file (e.g., `new_algorithm.py`).
2. Implement the algorithm.
3. Update `main.py` and `settings.py` to include the new method.
4. Define necessary helper functions inside `utils/`.

### Adding a New Problem
1. Define the problem’s fitness function in `fitness_functions.py`.
2. Modify `create_problem_sets.py` to generate test cases.
3. Ensure `settings.py` allows selecting the new problem.

---

## Example Output

### Genetic Algorithm on N-Queens
```
Generation 1: Best Fitness = 8
Generation 2: Best Fitness = 5
...
Solution Found: [4, 2, 0, 6, 1, 7, 5, 3]
```
*Interpreting Output*: The numbers represent queen placements in each row.

### PSO on Bin Packing
```
Iteration 1: Pack efficiency = 85%
Iteration 20: Pack efficiency = 97%
Optimal Packing Achieved!
```
*Interpreting Output*: The percentage represents the space utilization efficiency.

---

## Potential Use Cases

- **AI & Machine Learning**: Evolutionary algorithms can be used for hyperparameter tuning.
- **Operations Research**: Solving scheduling and packing problems.
- **Game Theory**: Applying Genetic Algorithms to AI-driven strategy games.
- **Computer Science Education**: Teaching optimization techniques.

---

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`feature-new-algorithm`).
3. Commit changes and push to GitHub.
4. Submit a pull request.

---

## License
This project is licensed under the **MIT License**, allowing open-source contributions and modifications.
