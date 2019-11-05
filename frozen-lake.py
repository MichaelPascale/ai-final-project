import gym

env = gym.make('FrozenLake-v0')

print(env.action_space.n)
print(env.observation_space.n)

