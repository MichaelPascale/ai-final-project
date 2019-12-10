# main.py
# Copyright 2019, Jonathan Lapham, Kyle Jolicoeur, and Michael Pascale. All rights reserved.
#
# Interfaces q-learning agent with particle-swarm-optimizer.

import qlearner
import PSO
import gym
from dataplotter import DataPlotter

e = gym.make('FrozenLake-v0')
episodes = 10000
q = qlearner.QLearner(e, episodes, 100)

#(lambda a, b : 3 + a ** 2 + b**2)
# -a ** 2 -b **2

# Setup the PSO algorithm and run
alpha = 0.5
gamma = 0.5
# list of lengthh 10000, 1 or 0. More 1s towards end of list.
# to graph, look at average over some increment.
# for example, graph the average over the first 1000 episodes, then the next.
# avg will be number in [0, 1]. This corresponds to "fitness"
InitialRewardPerEpisode = IR = q.run_session(alpha, gamma)
print ("Before tuning, QLearner achieves fitness of ", sum(IR[-1000:])/1000, "in 10,000 episodes.")

dataplot = DataPlotter()
# Eval function/fitness is average of the last 1000 episodes rewards.
# Should converge to ~0.7. In other words, gets a reward 70% of the time.
pso = PSO.ParticleSwarm((lambda a, b : sum(q.run_session(a, b)[-1000:])/1000), 5, 100, 0.00, 1.00, dataplot)
pso.minV = -1
pso.maxV = 1 
particles = [PSO.Particle(0.00, 1.00, dataplot) for _ in range(pso.numParticles)]

pso.particles = particles
pso.display_particles()
print("\n")
alpha, gamma = pso.algorithm()
FinalRewardPerEpisode = FR = q.run_session(alpha, gamma)
print ("After tuning, QLearner achieves fitness of ", sum(FR[-1000:])/1000, "in 10,000 episodes.")
dataplot.outputPSOGraphs()
