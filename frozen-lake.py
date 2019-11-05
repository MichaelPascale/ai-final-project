import gym

env = gym.make('FrozenLake-v0')

print("Action Space: ", env.action_space.n)
print("Observation Space: ", env.observation_space.n)

env.reset()

env.render()

print("observation, reward, done, info")
print(env.step(1))
