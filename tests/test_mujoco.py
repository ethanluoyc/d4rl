import gym
import d4rl # noqa


def test_mujoco_env():
    env = gym.make("hopper-medium-v2")
    env.reset()
    for _ in range(10):
        env.step(env.action_space.sample())

def test_kitchen():
    env = gym.make("kitchen-complete-v0")
    env.reset()
    for _ in range(10):
        env.step(env.action_space.sample())

def test_antmaze():
    env = gym.make("antmaze-umaze-v2")
    env.reset()
    for _ in range(10):
        env.step(env.action_space.sample())

def test_adroit():
    env = gym.make("door-human-v1")
    env.reset()
    for _ in range(10):
        env.step(env.action_space.sample())
