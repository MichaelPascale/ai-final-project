import gym

env = gym.make('FrozenLake-v0')

print("Action Space: ", env.action_space.n)
print("Observation Space: ", env.observation_space.n)

env.reset()

env.render()

print("observation, reward, done, info")
print(env.step(1))

# from deeplizard video https://youtu.be/QK_PP_2KgGE
import numpy
import gym
import random
import time
a_space_s = env.action_space.n
s_space_s = env.observation_space.n

# zeros creates a zero filled two dimensional array of Actions x States
qtable = numpy.zeros((s_space_s, a_space_s))
print(qtable)

# tunable parameters (genetic algorithms?)
episodes = 10000
steps = 100

l_rate = 0.1  # alpha
d_rate = 0.99 # gamma

e_rate = 1 # epsilon
max_e_rate = 1
min_e_rate = 0.01
e_decay_rate = 0.001

# from deeplizard video https://youtu.be/HGeI30uATws
# This implementation isn't too bad, but I'd prefer if we made it recursive. Thoughts?
all_rewards = []
# Q-Learning
for episode in range(episodes):
    # Reset the environment.
    state = env.reset()

    rewards = 0
    # time step in each episode
    for step in range(steps):
        e_rate_threshold = random.uniform(0, 1)
        if e_rate_threshold > e_rate:
            action = numpy.argmax(qtable[state, :]) # What does : mean in Python?
        else:
            action = env.action_space.sample()

        new_state, reward, done, info = env.step(action)
        env.render()

        qtable[state, action] = qtable[state, action] * (1 - l_rate) + l_rate * (reward + d_rate * numpy.max(qtable[new_state, :]))

        state = new_state
        rewards += reward

        if done == True:
            break

    # episode ends
    # exploration rate decays
    e_rate = min_e_rate + (max_e_rate - min_e_rate) * numpy.exp(-e_decay_rate * episode)
    all_rewards.append(rewards)

# all episodes done
# calculate average reward per 1000 episodes

R_per_KE = numpy.split(numpy.array(all_rewards), episodes/1000)
count = 1000
for r in R_per_KE:
    print(count, str(sum(r/1000)))
    count += 1000

print(qtable)



