import gym

env = gym.make('FrozenLake-v0')

print("Action Space: ", env.action_space.n)
print("Observation Space: ", env.observation_space.n)

env.reset()

env.render()

print("observation, reward, done, info")
print(env.step(1))

# from deeplizard video
import numpy
import gym
import random
import time
a_space_s = env.action_space.n
s_space_s = env.observation_space.n

# zeros creates a zero filled two dimensional array of Actions x States
qtable = numpy.zeros((s_space_s, a_space_s))
print(qtable)
