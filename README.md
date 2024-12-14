# RL Final Project - Dreamer V3

This is the repository with relevent code files for the submission of group 17 - "Mastering Diverse Domains through World Models - DreamerV3"

In this project we run and verify the dreamer V3 alogrithm and architechture proposed by [Hafner et al.](https://arxiv.org/pdf/2301.04104)

We run the algorithm for atari-MsPacman to verify existing results as well as FlappyBird, to verify performance on other relevent environments, comparing it to results from the PPO algorithm and a domain specific IRIS

## RUN instruaction

to run dreamer/ ppo algorithms usning sheeprl implementation use the following command inside the sheeprl directory
```bash
python sheeprl.py exp= path/to/exp.yaml
```

where exp can be one of the following:
- ppo_flappy
- ppo_pacman
- dreamer_v3_100k_ms_pacman
- dreamer_v3_flappy
- dreamer_v3_pacman_XS
- dreamer_v3_XS-flappy

to run inference of any of the above algorithms, with appropriate checkpoint, run the following command:
```bash
python sheeprl_eval.py checkpoint_path=path/to/checkpoint.ckpt
```

to view the tensorboard graphs run the following:
```bash
tensorboard --logdir= path/to/all/enclosing folder
```

Download all checkpoints and log files from the [drive](https://drive.google.com/drive/folders/16AAloH6p3BAfZ4nLNSepFxejm6z1avVR?usp=sharing) link