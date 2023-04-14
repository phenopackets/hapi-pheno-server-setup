import logging
import os
from pathlib import Path
import click
from typing import List, Optional
from .hapisetup import HapiSetup

logging.basicConfig(level=logging.INFO)

#
#
# def stop_hapi_setup_instance(sig, frame):
#     logging.info('======== Handling sig ================')
#     global hapi_setup_instance
#     hapi_setup_instance.close(sig)


# signal.signal(signal.SIGINT, stop_hapi_setup_instance)

hapi_setup_instance: Optional[HapiSetup] = None


@click.group(invoke_without_command=True)
@click.option('--profiles', envvar='HS_PROFILES')
@click.option('--setup-path', type=Path, default=Path.cwd())
@click.option('--restart_exit_code', type=int, default=10)
@click.option('--build-docker-image', is_flag=True)
@click.option('--build-hapi', is_flag=True)
@click.option('--stdout', is_flag=True)
@click.option('--stderr', is_flag=True)
def hapisetup(
        profiles: str,
        setup_path: Path,
        build_docker_image: bool,
        build_hapi: bool,
        stdout: bool,
        stderr: bool,
        restart_exit_code: int
):
    if profiles:
        os.environ['HS_PROFILES_CMDLINE'] = profiles

    exec(open(f'config/env-init.py').read())

    global hapi_setup_instance
    hapi_setup_instance = HapiSetup(setup_path=setup_path,
                                    build_docker_image=build_docker_image,
                                    build_hapi=build_hapi,
                                    stdout=stdout,
                                    stderr=stderr,
                                    restart_exit_code=restart_exit_code)


@hapisetup.command()
def env():
    for name, value in sorted(os.environ.items()):
        print("\t" + name + "=" + value)


@hapisetup.command(context_settings={"ignore_unknown_options": True})
@click.argument('params', nargs=-1)
def compose(params: List[str]):
    hapi_setup_instance.docker_compose(params)


# def hapi_setup_common_options(f):
#     @click.option('--setup-path', type=Path, default=Path.cwd())
#     @click.option('--restart_exit_code', type=int, default=10)
#     @click.option('--build-docker-image', is_flag=True)
#     @click.option('--build-hapi', is_flag=True)
#     @click.option('--stdout', is_flag=True)
#     @click.option('--stderr', is_flag=True)
#     @functools.wraps(f)
#     def wrapper_common_options(*args, **kwargs):
#         return f(*args, **kwargs)
#
#     return wrapper_common_options


@hapisetup.group()
def hapi():
    pass


@hapi.command(name='start')
# @hapi_setup_common_options
def hapi_start():
    logging.info('Start HAPI CLI')
    hapi_setup_instance.start()


@hapi.command(name='stop')
def hapi_stop():
    logging.info('Stopping HAPI CLI')
    hapi_setup_instance.stop()


@hapi.command(name='down')
def hapi_down():
    logging.info('Downing HAPI CLI')
    hapi_setup_instance.stop()
    hapi_setup_instance.down()


@hapi.command()
def load():
    hapi_setup_instance.hapi_load()
