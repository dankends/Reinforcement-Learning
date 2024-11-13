
# Reinforcement Learning Methods: Bandit Problem and Gridworld

This project explores reinforcement learning algorithms on two problems:
- The **Bandit Problem**: Implementing different exploration methods for multi-armed bandits.
- **Gridworld Environment**: Using dynamic programming (policy and value iteration) to find optimal policies.

## Table of Contents
- [Project Overview](#project-overview)
- [Methods](#methods)
- [Results](#results)
- [Setup Instructions](#setup-instructions)
- [Future Work](#future-work)

## Project Overview

This project contains two primary parts:
1. **Bandit Problem**: We examine ε-greedy, optimistic initial values, UCB, and gradient bandit methods.
2. **Gridworld**: Policy iteration and value iteration in a 5x5 grid environment with a terminal state.

Each part contains visualization and evaluation of cumulative rewards and regret.

## Methods

### Bandit Problem
The 10-armed bandit problem is solved using various methods:
- **ε-Greedy**: Balances exploration and exploitation.
- **Optimistic Initial Values**: Encourages initial exploration by setting optimistic values.
- **Upper Confidence Bound (UCB)**: Selects actions based on potential value and uncertainty.
- **Gradient Bandit**: Uses policy gradient with various learning rates.

### Gridworld
For a 5x5 grid environment:
- **Policy Iteration**: Iteratively improves policies based on the value function.
- **Value Iteration**: Finds optimal policies by maximizing state values.

## Results

- **Bandit Problem**: Each method's average reward and cumulative regret are plotted, showing differences in performance.
- **Gridworld**: The policies and value functions from policy and value iteration are visualized.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/dankends/HW1_Bandit_Problem_and_Gridworld.git
   cd HW1_Bandit_Problem_and_Gridworld
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Notebook**:
   - Open and run `HW1_cleaned.ipynb` in the `notebooks` folder to see the implementation and results.

## Future Work
- Experimenting with hyperparameter tuning.
- Testing additional exploration strategies.
