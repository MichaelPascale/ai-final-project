# qlearner.py
# Copyright 2019, Jonathan Lapham, Kyle Jolicoeur, and Michael Pascale. All rights reserved.
#
# Implements a Q-learning agent class with methods to run learning sessions and return
# performance statistics. Utilizes an OpenAI Gym as its environment (https://gym.openai.com/).
import random

class QLearner:
    # Initialize the q-learning agent to...
    def __init__(self, env, episodes = 999, steps_per_episode = 100):
        random.seed()

        self.env = env
        self.n_actions = env.action_space.n
        self.n_states  = env.observation_space.n
        self.n_episodes = episodes
        self.n_steps = steps_per_episode
        
        self.Q = [[0.0 for _ in range(self.n_actions)] for _ in range(self.n_states)]
        self.s = None
        self.a = None


    # Performance Statistics
    # Tuple of:
    #   List of average total reward per X episodes.
    #   What else do we want from this to analyze?
    
    # Decides exploration-exploitation.
    # Returns an action; either does so randomly or by selecting maximum Q.
    def explore(self, epsilon):
        if random.random() >= epsilon:
            actions = [action for action in range(self.n_actions)]
            return random.choice(actions)
        else:
            return max([a for a in range(self.n_actions)], key = lambda a : self.Q[self.s][a])


    # Update function, core q-learning algorithm.
    def update(self, s_, r_, alpha, gamma):
        self.Q[self.s][self.a] += alpha * (r_ + gamma * max(self.Q[s_][:]) - self.Q[self.s][self.a])


    # Run a single learning episode.
    def run_episode(self, epsilon, alpha, gamma):
        self.s = self.env.reset()

        for _ in range(self.n_steps):
            self.a = self.explore(epsilon)
            s_, r_, done, _ = self.env.step(self.a)
            if done:
                self.update(s_, r_, alpha, gamma)
                break
            #self.env.render()

            self.update(s_, r_, alpha, gamma)

            self.s = s_
        
        return sum(sum(self.Q, []))


    # Run a session of n_episodes.
    def run_session(self, epsilon = 0.2, alpha = 0.9, gamma = 0.90):
        self.reset()

        for _ in range(self.n_episodes):
            self.run_episode(epsilon, alpha, gamma)
        
        print(self.run_episode(epsilon, alpha, gamma))


    # Reset the agent to zero-knowledge.
    def reset(self):
        self.Q = [[0.0 for _ in range(self.n_actions)] for _ in range(self.n_states)]
        self.s = None
        self.a = None
