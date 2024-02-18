import gym
import d4rl # noqa
import numpy as np

def test_antmaze_randomness():
    env_name = "antmaze-umaze-v2"

    env1 = gym.make(env_name)
    env1.seed(seed=0)
    obs1 = env1.reset()

    env2 = gym.make(env_name)
    env2.seed(seed=0)
    obs2 = env2.reset()

    np.testing.assert_allclose(obs1, obs2)
