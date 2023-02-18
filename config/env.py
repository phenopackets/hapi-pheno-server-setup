import os
from os import environ
import pathlib
from pathlib import Path

environ['HAPISETUP_UID'] = environ.get('HAPISETUP_UID', str(os.getuid()))
environ['HAPISETUP_GID'] = environ.get('HAPISETUP_GID', str(os.getgid()))

environ['HAPISETUP_PG_IMAGE_DIR_DEFAULT'] = environ.get('HAPISETUP_PG_IMAGE_DIR_DEFAULT', str(Path('docker/image/_postgresql_default')))
environ['HAPISETUP_PG_IMAGE_DIR'] = environ.get('HAPISETUP_PG_IMAGE_DIR', environ['HAPISETUP_PG_IMAGE_DIR_DEFAULT'])
environ['HAPISETUP_PG_CONTAINER_DIR'] = environ.get('HAPISETUP_PG_CONTAINER_DIR', str(Path('docker/container/postgresql')))
environ['HAPISETUP_PG_PASSWORD'] = environ.get('HAPISETUP_PG_PASSWORD', 'postgres')
environ['HAPISETUP_PG_HOST'] = environ.get('HAPISETUP_PG_HOST', '127.0.0.1')
environ['HAPISETUP_PG_PORT'] = environ.get('HAPISETUP_PG_PORT', '15432')

# environ['HAPISETUP_TEST'] = environ.get('HAPISETUP_TEST', 'hapi test env value')
# environ['HAPISETUP_TEST'] = environ.get('HAPISETUP_TEST', 'hapi test env value')
# environ['HAPISETUP_TEST'] = environ.get('HAPISETUP_TEST', 'hapi test env value')
# environ['HAPISETUP_TEST'] = environ.get('HAPISETUP_TEST', 'hapi test env value')
# environ['HAPISETUP_TEST'] = environ.get('HAPISETUP_TEST', 'hapi test env value')
# environ['HAPISETUP_TEST'] = environ.get('HAPISETUP_TEST', 'hapi test env value')
