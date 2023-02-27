import click
from . import docker_compose, load_env


@click.group()
# @click.option('--profiles', envvar='HAPISETUP_PROFILES')
def hapisetup(**kwargs):
    load_env()

    # for name, value in sorted(os.environ.items()):
    #     print("   " + name + "=" + value)


# @hapisetup.command()
# def do_something():
#     print("Doing something")


# @hapisetup.group()
# def docker():


@hapisetup.group(context_settings={"ignore_unknown_options": True}, invoke_without_command=True)
@click.argument('params', nargs=-1)
def compose(params: list[str]):
    docker_compose(params)


@hapisetup.group()
def hapi():
    pass


@hapi.command()
def load():
    return docker_compose(['exec', 'hapi', 'hapisetup-hapi-load'])
