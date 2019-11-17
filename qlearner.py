# qlearner.py
# Copyright 2019, Jonathan Lapham, Kyle Jolicoeur, and Michael Pascale. All rights reserved.
#
# Implements a Q-learning agent class with methods to run learning sessions and return
# performance statistics. Utilizes an OpenAI Gym as its environment (https://gym.openai.com/).
import random

class QLearner:
    # Initialize the q-learning agent to...
    def __init__(self, env, episodes, steps_per_episode):
        self.env = env
        self.n_actions = env.action_space.n
        self.n_states  = env.observation_space.n
        self.n_episodes = episodes
        self.n_steps = steps_per_episode
        self.qtable = []

    # Performance Statistics
    # Tuple of:
    #   List of average total reward per X episodes.
    #   What else do we want from this to analyze?

    # Run a single learning episode.
    # Returns performance statistics.
    def run_episode(self, epsilon, alpha, gamma):
        pass

    # Run a session of n_episodes.
    # Returns performance statistics.
    def run_session(self, epsilon, alpha, gamma):
        pass

    # Reset the agent to zero-knowledge.
    def reset(self):
        pass
