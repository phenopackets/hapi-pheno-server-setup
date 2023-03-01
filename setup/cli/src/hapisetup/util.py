import os
from os import environ
import subprocess
from pathlib import Path
from typing import Mapping, List


def run_subprocess(command: List[str], evn: Mapping):
    return subprocess.run(command, env=evn)


def init_env():
    exec(open(f'config/env-init.py').read())
    init_local_path = Path('config/env-init-local.py')
    if init_local_path.exists():
        exec(open(init_local_path).read())

def load_env():
    for env in os.environ['HS_PROFILES'].split(','):
        if not env:
            continue
        env_path = Path(f'config/{env}.py').absolute()
        print(f'Attempting to load environment file: {env_path}')
        if env_path.exists():
            print(f'Loading environment file: {env}')
            exec(open(f'config/{env}.py').read())


def docker_compose(args: List[str]):
    compose = ['docker', 'compose']
    for profile in environ['HS_PROFILES'].split(','):
        compose.extend(['--profile', profile])
    compose.extend(args)
    print(f'Running: {compose}')
    return run_subprocess(compose, os.environ)
