import qlearner
import gym
e = gym.make('FrozenLake-v0')
q = qlearner.QLearner(e)
q.run_session()

