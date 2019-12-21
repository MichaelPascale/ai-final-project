# ql-stats.py
# Copyright 2019, Michael Pascale. All rights reserved.
#
# Just print some statistics to graph Q-learner progress.

import qlearner
import gym
import random
import statistics

sessions = 50
episodes = 20000
episodes_to_avg = 1000
alpha = 0.04180932
gamma = 0.93332194

e = gym.make('FrozenLake-v0')
q = qlearner.QLearner(e, episodes, 100)

list_of_rewards = []
for i in range(sessions):
    print("Session", i, "of", sessions, flush=True, end='')
    list_of_rewards.append(q.run_session(alpha, gamma))
    #list_of_rewards.append(q.run_session(random.random(), random.random()))
    print("\r", flush=True, end='')

sum_rewards = {}
for rewards in list_of_rewards:
    for episode in range(len(rewards)):
        sum_rewards[episode] = sum_rewards.get(episode, 0.0) + rewards[episode]

avg_rewards = list(map(lambda x : x/sessions, sum_rewards.values()))
std_devs = [statistics.stdev(r_tuple) for r_tuple in list(zip(*list_of_rewards))]

print("Sums of the rewards earned over each", episodes_to_avg, "of", episodes, "episodes, rewards averaged over", sessions, "sessions.")
for i in range(len(avg_rewards)):
    if ((i + 1) % episodes_to_avg is 0) and (i > 0):
        print(i, sum(avg_rewards[i-episodes_to_avg:i])/episodes_to_avg, sum(std_devs[i-episodes_to_avg:i])/episodes_to_avg)
        