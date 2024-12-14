import flappy_bird_gymnasium
import gymnasium as gym


class FlappyBirdWrapper(gym.Wrapper):
    def __init__(self, seed: int = None):
        env = gym.make("FlappyBird-v0", render_mode="rgb_array", use_lidar=False)
        super().__init__(env)
        self.observation_space = env.observation_space
        self.action_space = env.action_space

    def step(self, action):
        return  self.env.step(action)

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
        return