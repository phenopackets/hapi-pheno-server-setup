import os
from os import environ
import subprocess
from pathlib import Path


def load_env():
    # load the env stub file to find any more profiles to load
    exec(open(str(Path('config/env.py'))).read())

    # load any profiles
    clean_prfiles = list(filter(None, [profile.strip() for profile in environ.get('HAPISETUP_PROFILES').split(',')]))
    environ['HAPISETUP_PROFILES'] = ','.join(clean_prfiles)
    print(f"PROFILES: {environ['HAPISETUP_PROFILES']}")
    for profile in clean_prfiles:
        profile_path = Path(f'config/env-{profile}.py').absolute()
        print(f'Attempting to load profile: {profile_path}')
        if profile_path.exists():
            print(f'Loading profile: {profile}')
            exec(open(f'config/env-{profile}.py').read())


def docker_compose(args: list[str]):
    compose = ['docker', 'compose']
    compose.extend(args)
    return subprocess.run(compose, env=os.environ)
