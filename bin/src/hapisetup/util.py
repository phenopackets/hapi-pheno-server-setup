import os
import subprocess
from pathlib import Path


def load_env(profiles=None):
    if profiles is not None:
        for profile in profiles:
            exec(open(f'config/env-${profile}.py').read())
    getcwd = os.getcwd()
    print(getcwd)
    exec(open(str(Path('config/env.py'))).read())


def docker_compose(args: list[str]):
    compose = ['docker', 'compose']
    compose.extend(args)
    return subprocess.run(compose, env=os.environ)
