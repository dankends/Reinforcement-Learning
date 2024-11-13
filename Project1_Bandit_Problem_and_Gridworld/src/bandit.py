
import numpy as np
import matplotlib.pyplot as plt
import random

class Bandit:
    def __init__(self):
        self.q_true = np.random.normal(0, 1, 10)
        self.q_estimate = np.zeros(10)
        self.action_count = np.zeros(10)
        
    def pull(self, action):
        reward = np.random.normal(self.q_true[action], 1)
        return reward

    def update_estimates(self, action, reward):
        self.action_count[action] += 1
        self.q_estimate[action] += (1 / self.action_count[action]) * (reward - self.q_estimate[action])

def epsilon_greedy(bandit, epsilon, n_pulls=1000):
    rewards = []
    for _ in range(n_pulls):
        if random.random() < epsilon:
            action = random.randint(0, 9)
        else:
            action = np.argmax(bandit.q_estimate)
        reward = bandit.pull(action)
        bandit.update_estimates(action, reward)
        rewards.append(reward)
    return np.cumsum(rewards) / (np.arange(n_pulls) + 1)

# Example plot function
def plot_rewards(rewards, labels):
    for i, reward in enumerate(rewards):
        plt.plot(reward, label=labels[i])
    plt.xlabel("Steps")
    plt.ylabel("Average Reward")
    plt.legend()
    plt.show()
