import gym
import d4rl # noqa
import pytest

ALL_TEST_ENVS = []
for env_name in d4rl.infos.DATASET_URLS.keys():
    if env_name.startswith(('carla', 'flow', 'minigrid', 'bullet')):
        continue
    else:
        ALL_TEST_ENVS.append(env_name)

@pytest.mark.parametrize("env_name", ALL_TEST_ENVS)
def test_all_envs(env_name):
    env = gym.make(env_name)
    env.reset()
    for _ in range(10):
        env.step(env.action_space.sample())
