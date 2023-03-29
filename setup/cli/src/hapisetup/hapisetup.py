import logging
import subprocess
from os import environ
from pathlib import Path
from subprocess import Popen
from typing import List, Optional

from hapisetup import docker_compose


class HapiSetup:
    def __init__(self,
                 setup_path: Path,
                 build_docker_image: bool,
                 build_hapi: bool,
                 stdout: bool,
                 stderr: bool,
                 restart_exit_code: int
                 ):
        self._setup_path = setup_path
        self._build_docker_image = build_docker_image
        self._build_hapi = build_hapi
        self._stdout = stdout
        self._stderr = stderr
        self._restart_exit_code = restart_exit_code
        self._popen: Popen = None

    def start(self):
        logging.info('Starting HAPI')
        while True:
            self._popen = self.build_hapi()
            if self._popen:
                self._popen.wait()
            logging.info('Finished building HAPI')
            self._popen = self.run_hapi()
            if self._popen.wait() != self._restart_exit_code:
                break

    def stop(self):
        logging.info("Stopping HAPI")
        self.docker_compose(['down']).wait()

    def build_hapi(self) -> Optional[Popen]:
        if not self.build_hapi:
            return None
        args = ['run', '--rm']
        if self._build_docker_image:
            args.append('--build')
        args.append('hapi-build')
        return self.docker_compose(args)

    def run_hapi(self) -> Popen:
        args = ['up', '--exit-code-from', 'hapi']
        if self._build_docker_image:
            args.append('--build')
        return self.docker_compose(args)

    def docker_compose(self, args: List[str]) -> Popen:
        compose = ['docker', 'compose']
        for profile in environ['HS_PROFILES'].split(','):
            compose.extend(['--profile', profile])
        compose.extend(args)

        kwargs = {
            'stdout': subprocess.DEVNULL,
            'stderr': subprocess.DEVNULL
        }

        if self._stdout:
            kwargs['stdout'] = None
        if self._stderr:
            kwargs['stderr'] = None

        popen = Popen(compose, env=environ, **kwargs)
        return popen

    def close(self, sig):
        self._popen.send_signal(sig)
