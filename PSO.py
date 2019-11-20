'''
Created on Nov 18, 2019

@author: Jonathan Lapham
'''
import numpy as np
from random import randrange


class Particle():

	# Initializes the particle itself
    def __init__(self, minRange, maxRange):
        # self.position = np.array([randrange(minRange, maxRange, 1)*0.01,randrange(minRange, maxRange, 1)*0.01])
        self.position = np.array([randrange(minRange, maxRange, 1),randrange(minRange, maxRange, 1)])
        self.velocity = np.array([0,0])
        self.fitness = float("inf")
        self.bestPosition = self.position
        self.bestFitness = float('inf')
        self.min = minRange
        self.max = maxRange
    
	# Prints the particle 
    def __str__(self):
        print("Particle is at ", self.position, " my best position is ", self.bestPosition)
        
	# Moves a single particle 
    def move(self):
        self.position = self.position + self.velocity
        self.check_range(self.position, self.min, self.max)

	# Used to set the check and limit the range of the swarm
    def check_range(self, value, minimum, maximum):
        if value[0] > maximum:
            value[0] = maximum
        elif value[0] < minimum:
            value[0] = minimum
        if value[1] > maximum:
            value[1] = maximum
        elif value[1] < minimum:
            value[1] = minimum
            

class ParticleSwarm():
    def __init__(self, numParticles, numIterations, minRange, maxRange):
        # Initializes PSO algorithm values 
        
        # Inertia 
        self.w = 0.729
        # personal weight
        self.c1 = 1.49445
        # global weight
        self.c2 = 1.49445
        # Random variables (helps with getting stuck)
        self.r1 = 0
        self.r2 = 0
        
        # Handles testing arguements
        self.numberIterations = numIterations
        self.iteration = 0
        self.minX = minRange
        self.maxX = maxRange

        self.minV = minRange
        self.maxV = maxRange        
        # Handles Initializing PSO space
        self.numParticles = numParticles
        self.particles = []
        self.global_best_fitness = float('inf')
        # self.global_best_position = np.array([randrange(minRange,maxRange,1)*0.01,randrange(minRange,maxRange,1)*0.01])
        self.global_best_position = np.array([float('inf'),float('inf')])

	# Simply displays a list of particles and their position
    def display_particles(self):
        for particle in self.particles:
            particle.__str__()
            
	# The evaluation function
    def fitness_evaluation(self, particle):
        fitness = 3 + particle.position[0] ** 2 + particle.position[1]**2
        return fitness

	# Runs the evaluation function for every particle
    def eval_all(self):
        for particle in self.particles:
            particle.fitness = self.fitness_evaluation(particle)

	# Acquires the best position for a single particle
    def set_personal_best(self):
        for particle in self.particles:   
            # CHANGES IF YOU WANT TO FIND MINIMUM OR MAXIMUM
            # it is set to minimum 
            if (particle.fitness < particle.bestFitness):
                particle.bestFitness = particle.fitness
                particle.bestPosition = particle.position
                
	# Acquires the best position out of all particles
    def set_global_best(self):
        for particle in self.particles:      
            # CHANGES IF YOU WANT TO FIND MINIMUM OR MAXIMUM
            # it is set to minimum 
            if (particle.fitness < self.global_best_fitness):
                self.global_best_fitness = particle.fitness
                self.global_best_position = particle.position
            
	# Updates the velocity of each particle acccordingly, then moves the particles
    def move_particles(self):
        for particle in self.particles:
            self.r1 = randrange(0,100,1)*0.01
            self.r2 = randrange(0,100,1)*0.01

			# v(t+1) = (w * v(t)) + (c1 * r1 * (p(t) – x(t)) + (c2 * r2 * (g(t) – x(t))
            new_velocity = (self.w * particle.velocity) + (self.c1 * self.r1 * (particle.bestPosition - particle.position)) + \
                            (self.c2 * self.r2 * (self.global_best_position - particle.position))

            particle.check_range(new_velocity, self.minV, self.maxV)

            particle.velocity = new_velocity
            particle.move()

	# The algorithm itself, follows flow chart on proposoal
    def algorithm(self):
        while(self.iteration < self.numberIterations):
            self.eval_all()
            self.set_personal_best()
            self.set_global_best()
            self.move_particles()
            self.iteration += 1
            print("iteration number ", self.iteration)
            self.display_particles()
            print("\n")

        print("The best position is ", self.global_best_position, "in iteration number ", self.iteration)


if __name__ == "__main__":

    # Setup the PSO algorithm and run
    state_space = ParticleSwarm(5, 100, -100, 100)
    particles_vector = [Particle(-100, 100) for _ in range(state_space.numParticles)]
    state_space.particles = particles_vector
    state_space.display_particles()
    print("\n")
    state_space.algorithm()




    
    
    
    
        
    
        
    
        
        
        