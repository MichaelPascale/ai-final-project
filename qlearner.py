# qlearner.py
# Copyright 2019, Jonathan Lapham, Kyle Jolicoeur, and Michael Pascale. All rights reserved.
#
# Implements a Q-learning agent class with methods to run learning sessions and return
# performance statistics. Utilizes an OpenAI Gym as its environment (https://gym.openai.com/).
import random

class QLearner:
    # Initialize the q-learning agent to...
    def __init__(self, env, episodes = 100, steps_per_episode = 100):
        random.seed()

        self.env = env
        self.n_actions = env.action_space.n
        self.n_states  = env.observation_space.n
        self.n_episodes = episodes
        self.n_steps = steps_per_episode
        
        self.Q = None
        self.N = None
        self.prev_state = None
        self.prev_action = None
        self.prev_reward = None

    # Performance Statistics
    # Tuple of:
    #   List of average total reward per X episodes.
    #   What else do we want from this to analyze?
    
    # Decides exploration-exploitation.
    # Returns an action.
    def explore(self, epsilon):
        if self.Q is None or random.random() >= epsilon:
            actions = [action for action in range(self.n_actions)]
            return random.choice(actions)
        else:
            return max([a for a in range(self.n_actions)], key = lambda a : self.Q[self.prev_state][a])


    # Update function, core q-learning algorithm.
    def update(self, s, a, r, alpha, gamma): # * self.N[s][a] *
        self.Q[s][a] = self.Q[s][a] + alpha * (r + gamma * max(self.Q[s][:]))
        print(self.Q)

    # Run a single learning episode.
    # Returns performance statistics.
    def run_episode(self, epsilon, alpha, gamma):

        self.prev_state = self.env.reset()

        for _ in range(self.n_steps):
            action = self.explore(epsilon)
            state, reward, done, info = self.env.step(action)
            if done:
                self.update(state, action, reward, alpha, gamma)
                break
            #self.env.render()

            self.update(state, action, reward, alpha, gamma)

            self.prev_state = state
            self.prev_action = action
            self.prev_reward = reward

    # Run a session of n_episodes.
    # Returns performance statistics.
    def run_session(self, epsilon = 0.5, alpha = 0.5, gamma = 1):
        
        self.reset()
        self.env.reset()
        for _ in range(self.n_episodes):
            self.run_episode(epsilon, alpha, gamma)

    # Reset the agent to zero-knowledge.
    def reset(self):
        self.Q = [[0.0 for _ in range(self.n_actions)] for _ in range(self.n_states)]
        self.N = [[0.0 for _ in range(self.n_actions)] for _ in range(self.n_states)]
        self.prev_state = None
        self.prev_action = None
        self.prev_reward = None
