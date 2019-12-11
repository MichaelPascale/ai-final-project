# main.py
# Copyright 2019, Jonathan Lapham, Kyle Jolicoeur, and Michael Pascale. All rights reserved.
#
# Interfaces q-learning agent with particle-swarm-optimizer.

import qlearner
import PSO
import gym
import random
from dataplotter import DataPlotter

e = gym.make('FrozenLake-v0')
episodes = 10000
q = qlearner.QLearner(e, episodes, 100)

#(lambda a, b : 3 + a ** 2 + b**2)
# -a ** 2 -b **2

# Setup the PSO algorithm and run
alpha = 0
gamma = 0
# list of lengthh 10000, 1 or 0. More 1s towards end of list.
# to graph, look at average over some increment.
# for example, graph the average over the first 1000 episodes, then the next.
# avg will be number in [0, 1]. This corresponds to "fitness"

IR = [q.run_session(random.random(), random.random()) for _ in range(30)]
IRAvg = sum([sum(i[-1000:])/1000 for i in IR])/10

InitialRewardPerEpisode = IR
print ("Before tuning, QLearner achieves averages fitness of ", IRAvg, "in 30 runs of 10,000 episodes.")

dataplot = DataPlotter()
# Eval function/fitness is average of the last 1000 episodes rewards.
# Should converge to ~0.7. In other words, gets a reward 70% of the time.
pso = PSO.ParticleSwarm((lambda a, b : sum(q.run_session(a, b)[-1000:])/1000), 5, 100, 0.00, 1.00, dataplot)
pso.minV = -1
pso.maxV = 1 
particles = [PSO.Particle(0.00, 1.00, dataplot) for _ in range(pso.numParticles)]
pso.particles = particles
pso.display_particles()
alpha, gamma = pso.algorithm()

FR = [q.run_session(alpha, gamma) for _ in range(30)]
FRAvg = sum([sum(i[-1000:])/1000 for i in FR])/10

FinalRewardPerEpisode = FR
print ("After tuning, QLearner achieves average fitness of ", FRAvg, "in 30 runs of 10,000 episodes.")
dataplot.appendqlRVals(IR, FR)
dataplot.outputGraphs()
