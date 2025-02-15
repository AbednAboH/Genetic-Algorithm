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

### Example: Running the Genetic Algorithm
If `settings.py` is configured to use the Genetic Algorithm for the N-Queens problem, running:
```bash
python main.py
```
will execute the algorithm and output the results.

---

## License
This project is licensed under the **MIT License**, allowing open-source contributions and modifications.
