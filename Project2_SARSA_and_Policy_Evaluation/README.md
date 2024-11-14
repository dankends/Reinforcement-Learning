Reinforcement Learning on FrozenLake Environment
================================================

This project demonstrates the use of various Reinforcement Learning (RL)
algorithms in navigating a slippery grid environment, known as FrozenLake,
implemented using OpenAI Gym. The goal is to help an agent learn to avoid holes
in the lake, reach the goal tile, and do so as efficiently as possible.

Table of Contents
-----------------

-   [Project Overview](#project-overview)

-   [Environment Details](#environment-details)

-   [Implemented Algorithms](#implemented-algorithms)

-   [Project Structure](#project-structure)

-   [Installation](#installation)

-   [Usage](#usage)

-   [Results](#results)

-   [Conclusions](#conclusions)

Project Overview
----------------

This project was developed as part of an assignment to implement several RL
algorithms on a modified version of the FrozenLake environment. The algorithms
implemented include Monte Carlo methods, Temporal Difference (TD) learning, and
control methods, each with the goal of training an agent to efficiently navigate
the environment.

Environment Details
-------------------

-   **Environment**: FrozenLake (4x4 grid)

-   **Actions**: Left, Down, Right, Up

-   **Rewards**:

    -   Reaching the goal: 0

    -   Falling into a hole: -100

    -   Maximum step limit (100 steps): -50

    -   Every other step: -1

-   **Discount Factor**: 0.99

-   **Slip Rate**: 0.1 (probability of unintended movement)

Implemented Algorithms
----------------------

1.  **Monte Carlo Methods**

    -   First-Visit Monte Carlo

    -   Off-policy Importance Sampling (ordinary and weighted)

2.  **Temporal Difference (TD) Learning**

    -   Every-Visit Monte Carlo

    -   TD(0)

    -   n-step TD

3.  **Control Methods**

    -   SARSA

    -   Expected SARSA

    -   Q-Learning

Project Structure
-----------------

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ plaintext
RL-FrozenLake-Project/
├── notebooks/
│   └── RL_FrozenLake_Project.ipynb   # Main Jupyter Notebook with code and outputs
├── README.md                         # Project readme file
└── requirements.txt                  # Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Installation
------------

1.  Clone this repository:

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ bash
    git clone https://github.com/dankends/Reinforcement-Learning/Project2_SARSA_and_Policy_Evaluation.git
    cd RL-FrozenLake-Project
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

2.  Install dependencies:

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ bash
    pip install -r requirements.txt
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

3.  Ensure `gym` and `numpy` are installed. The FrozenLake environment can be
    imported from OpenAI Gym:

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ python
    import gym
    env = gym.make("FrozenLake-v1", is_slippery=True)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Usage
-----

Open the notebook in Jupyter:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ bash
jupyter notebook notebooks/Notebook.ipynb
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow the cells in the notebook to execute each part of the project
step-by-step.

Results
-------

The notebook includes visualizations of: - Learning curves for each state under
different algorithms - Comparison plots between different RL methods -
Performance metrics of each control method

Conclusions
-----------

This project illustrates the strengths and weaknesses of different RL methods
applied to the FrozenLake environment. Monte Carlo methods converge slower but
are unbiased, while TD methods show faster convergence but may introduce bias
due to bootstrapping. Control methods like SARSA, Expected SARSA, and Q-Learning
offer various trade-offs in exploration vs. exploitation.
