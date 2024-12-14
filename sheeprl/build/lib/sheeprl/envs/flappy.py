import flappy_bird_gym
import gymnasium as gym
import numpy as np

class FlappyBirdWrapper(gym.Wrapper):
    def __init__(self, seed: int = None):
        env = flappy_bird_gym.make("FlappyBird-v0")
        super().__init__(env)
        self.observation_space = env.observation_space
        self.action_space = env.action_space

    def step(self, action):
        obs, reward, done, info = self.env.step(action)
        return obs, reward, done, False, info

    def reset(self, seed=None, options=None):
        obs, info = self.env.reset()
        return obs, info
    
    @property
    def render_mode(self) -> str | None:
        return self.env._render_mode

    def render(self):
        return self.env.render()

    def close(self):
        self.env.close()