import os

import click
from . import docker_compose, load_env, init_env
from typing import List


@click.group()
@click.option('--profiles', envvar='HS_PROFILES')
def hapisetup(profiles: str):
    if profiles:
        os.environ['HS_PROFILES_CMDLINE'] = profiles
    init_env()
    load_env()


@hapisetup.command()
def env():
    for name, value in sorted(os.environ.items()):
        print("\t" + name + "=" + value)


@hapisetup.group(context_settings={"ignore_unknown_options": True}, invoke_without_command=True)
@click.argument('params', nargs=-1)
def compose(params: List[str]):
    docker_compose(params)


@hapisetup.group()
def hapi():
    pass


@hapi.command()
def load():
    return docker_compose(['exec', 'hapi', 'hapisetup-hapi-load'])
