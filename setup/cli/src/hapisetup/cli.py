import logging
import os
import sys
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

hs: Optional[HapiSetup] = None


@click.group(invoke_without_command=True)
@click.option('--profiles', envvar='HS_PROFILES')
@click.option('--no-profiles', is_flag=True)
@click.option('--setup-path', type=Path, default=Path.cwd())
@click.option('--build-docker-image', is_flag=True)
@click.option('--build-hapi', is_flag=True)
@click.option('--no-out', is_flag=True)
@click.option('--no-err', is_flag=True)
@click.option('--restart_exit_code', type=int, default=10)
@click.option('--debug', is_flag=True)
@click.option('--attach', '-d', is_flag=True)
def hapisetup(
        profiles: str,
        no_profiles: bool,
        setup_path: Path,
        build_docker_image: bool,
        build_hapi: bool,
        no_out: bool,
        no_err: bool,
        restart_exit_code: int,
        debug: bool,
        attach: bool
):
    root = logging.getLogger()
    root.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)

    if debug:
        root.setLevel(logging.DEBUG)
        handler.setLevel(logging.DEBUG)

    if profiles:
        os.environ['HS_PROFILES_CMDLINE'] = profiles

    if no_profiles:
        os.environ['HS_PROFILES_CMDLINE'] = ''

    exec(open(f'config/env-init.py').read())

    global hs
    hs = HapiSetup(setup_path=setup_path,
                   build_docker_image=build_docker_image,
                   build_hapi=build_hapi,
                   stdout=not no_out,
                   stderr=not no_err,
                   restart_exit_code=restart_exit_code,
                   debug=debug,
                   attach=attach)


# =========================
# General commands
# =========================

@hapisetup.command(name='start')
def hs_start():
    logging.info('Running compose up hapi')
    hs.start()


@hapisetup.command(name='stop')
def hs_stop():
    logging.info('Running compose stop')
    hs.stop()


@hapisetup.command(name='down')
def hs_down():
    logging.info('Running compose down')
    hs.stop()
    hs.down()


@hapisetup.command(name='compose', context_settings=dict(
    ignore_unknown_options=True,
    allow_extra_args=True,
))
@click.pass_context
def hs_compose(ctx):
    """Simply runs docker compose with the command line args specified."""
    hs.compose(ctx.args)


@hapisetup.command(name='env')
def hs_env():
    """Show the effective environment."""
    for name, value in sorted(os.environ.items()):
        print("\t" + name + "=" + value)


@hapisetup.command(name='reset')
@click.option('--pg', is_flag=True)
@click.option('--es', is_flag=True)
@click.option('--hapi-target', is_flag=True)
@click.option('--hapi-logs', is_flag=True)
@click.option('--hapi-loaders', is_flag=True)
# @click.option('--hapi-build', is_flag=True)
# @click.option('--hapi-build-m2', is_flag=True)
def hs_reset(**kwargs):
    print(kwargs)
    hs.reset(**kwargs)


# =========================
#
# =========================


# =========================
# Postgresql commands
# =========================

@hapisetup.group(name='pg')
def postgresql():
    """Postgresql specific subcommands"""
    pass


@postgresql.command(name='up')
def postgresql_start():
    hs.postgresql_up()


@postgresql.command(name='stop')
def postgresql_stop():
    hs.postgresql_stop()


@postgresql.command(name='remove')
def postgresql_remove():
    """Stops and removes the Postgresql container"""
    hs.postgresql_stop()
    hs.postgresql_remove()


# =========================
# Elasticsearch commands
# =========================


@hapisetup.group(name='es')
def elasticsearch():
    """Elasticsearch specific subcommands"""
    pass


@elasticsearch.command(name='up')
def elasticsearch_start():
    """Start Elasticsearch"""
    hs.elasticsearch_up()


@elasticsearch.command(name='stop')
def elasticsearch_stop():
    """Stop Elasticsearch"""
    hs.elasticsearch_stop()


@elasticsearch.command(name='remove')
def elasticsearch_remove():
    """Stops and removes the Elasticsearch container"""
    hs.elasticsearch_stop()
    hs.elasticsearch_remove()


# =========================
# Kibana commands
# =========================

@hapisetup.group(name='kibana')
def kibana():
    """Kibana specific subcommands"""
    pass


@kibana.command(name='up')
def kibana_start():
    """Up the Kibana container"""
    hs.kibana_up()


@kibana.command(name='stop')
def kibana_stop():
    """Stop Kibana container"""
    hs.kibana_stop()


@kibana.command(name='remove')
def kibana_remove():
    """Stops and removes the Kibana container"""
    hs.kibana_stop()
    hs.kibana_remove()


# =========================
# HAPI commands
# =========================


@hapisetup.group()
def hapi():
    pass


@hapi.command(name='load')
def load():
    hs.hapi_load()


# =========================
# Hidden
# =========================


@hapisetup.command(hidden=True)
@click.option('--arg', multiple=True, default=[])
def test(arg):
    print(f'Value: {arg}')
    print(f'Type: {type(arg)}')
