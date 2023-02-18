import os
import click
from . import docker_compose, load_env


@click.group()
@click.option('--message')
@click.option('--env-profile', type=str, default=[], help='The environment profiles to load, in order. '                                                   'files like config/env-profile.py will be loaded as python scripts, in order')
def hapisetup(**kwargs):
    print("Python hapisetup: " + str(kwargs))
    load_env()

    for name, value in sorted(os.environ.items()):
        print("   " + name + "=" + value)


@hapisetup.command()
def do_something():
    print("Doing something")


@hapisetup.group()
def docker():
    print('Doing docker')


@docker.group(context_settings={"ignore_unknown_options": True}, invoke_without_command=True)
@click.argument('params', nargs=-1)
def compose(params: list[str]):
    print('Doing compose')
    docker_compose(params)


# @compose.command()
# @click.argument('params', nargs=-1)
# def up(params: list[str]):
#     docker_compose(params)
