
import numpy as np

class Gridworld:
    def __init__(self, size=5):
        self.size = size
        self.state_values = np.zeros((size, size))
        self.policy = np.full((size, size), 'up')

    def policy_evaluation(self, gamma=1.0, theta=0.01):
        delta = theta
        while delta >= theta:
            delta = 0
            for i in range(self.size):
                for j in range(self.size):
                    v = self.state_values[i, j]
                    new_value = self.calculate_value(i, j, gamma)
                    delta = max(delta, abs(new_value - v))
                    self.state_values[i, j] = new_value

    def calculate_value(self, i, j, gamma):
        reward = -1
        value = 0
        transitions = self.get_transitions(i, j)
        for (new_i, new_j) in transitions:
            value += 0.25 * (reward + gamma * self.state_values[new_i, new_j])
        return value

    def get_transitions(self, i, j):
        return [
            (max(0, i - 1), j),
            (min(self.size - 1, i + 1), j),
            (i, max(0, j - 1)),
            (i, min(self.size - 1, j + 1))
        ]
