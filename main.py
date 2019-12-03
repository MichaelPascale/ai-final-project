# main.py
# Copyright 2019, Jonathan Lapham, Kyle Jolicoeur, and Michael Pascale. All rights reserved.
#
# Interfaces q-learning agent with particle-swarm-optimizer.

import qlearner
import PSO
import gym

e = gym.make('FrozenLake-v0')
q = qlearner.QLearner(e, 10000, 100)

#(lambda a, b : 3 + a ** 2 + b**2)
# -a ** 2 -b **2

# Setup the PSO algorithm and run
pso = PSO.ParticleSwarm((lambda a, b : q.run_session(a, b)), 5, 100, 0.00, 1.00)
pso.minV = -1
pso.maxV = 1 
particles = [PSO.Particle(0.00, 1.00) for _ in range(pso.numParticles)]
pso.particles = particles
pso.display_particles()
print("\n")
pso.algorithm()