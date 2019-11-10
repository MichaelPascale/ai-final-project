import gym

env = gym.make('SpaceInvaders-ram-v0')
env.reset()

while (True):
    done = False
    while (not done):
        observation, reward, done, info = env.step(env.action_space.sample())
        env.render()
        print(observation, reward, done, info)