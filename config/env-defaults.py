import os
import shutil
from os import environ
import pathlib
from pathlib import Path

environ['HAPISETUP_UID'] = environ.get('HAPISETUP_UID', str(os.getuid()))
environ['HAPISETUP_GID'] = environ.get('HAPISETUP_GID', str(os.getgid()))

environ['HAPISETUP_PG_IMAGE_DIR_DEFAULT'] = environ.get('HAPISETUP_PG_IMAGE_DIR_DEFAULT', str(Path('setup/docker_image/_postgresql_default')))
environ['HAPISETUP_PG_IMAGE_DIR'] = environ.get('HAPISETUP_PG_IMAGE_DIR', environ['HAPISETUP_PG_IMAGE_DIR_DEFAULT'])
environ['HAPISETUP_PG_CONTAINER_DIR'] = environ.get('HAPISETUP_PG_CONTAINER_DIR', str(Path('setup/docker_container/postgresql')))
environ['HAPISETUP_PG_PASSWORD'] = environ.get('HAPISETUP_PG_PASSWORD', 'postgres')
environ['HAPISETUP_PG_HOST'] = environ.get('HAPISETUP_PG_HOST', '127.0.0.1')
environ['HAPISETUP_PG_PORT'] = environ.get('HAPISETUP_PG_PORT', '15432')

if not Path(environ['HAPISETUP_PG_IMAGE_DIR']).is_dir():
    shutil.copytree(environ['HAPISETUP_PG_IMAGE_DIR_DEFAULT'] , environ['HAPISETUP_PG_IMAGE_DIR'])
(Path(environ['HAPISETUP_PG_CONTAINER_DIR'])/'data-volume').mkdir(parents=True, exist_ok=True)


environ['HAPISETUP_ESREST_IMAGE_DIR_DEFAULT'] = environ.get('HAPISETUP_ESREST_IMAGE_DIR_DEFAULT', str(Path('setup/docker_image/_elasticsearch_default')))
environ['HAPISETUP_ESREST_IMAGE_DIR'] = environ.get('HAPISETUP_ESREST_IMAGE_DIR', environ['HAPISETUP_ESREST_IMAGE_DIR_DEFAULT'])
environ['HAPISETUP_ESREST_CONTAINER_DIR'] = environ.get('HAPISETUP_ESREST_CONTAINER_DIR', str(Path('setup/docker_container/elasticsearch')))
environ['HAPISETUP_ESREST_PASSWORD'] = environ.get('HAPISETUP_ESREST_PASSWORD', 'elastic')
environ['HAPISETUP_ESREST_HOST'] = environ.get('HAPISETUP_ESREST_HOST', '127.0.0.1')
environ['HAPISETUP_ESREST_PORT'] = environ.get('HAPISETUP_ESREST_PORT', '19200')
if not Path(environ['HAPISETUP_ESREST_IMAGE_DIR']).is_dir():
    shutil.copytree(environ['HAPISETUP_ESREST_IMAGE_DIR_DEFAULT'] , environ['HAPISETUP_ESREST_IMAGE_DIR'])
(Path(environ['HAPISETUP_ESREST_CONTAINER_DIR'])/'data-volume').mkdir(parents=True, exist_ok=True)


environ['HAPISETUP_KIBANA_IMAGE_DIR_DEFAULT'] = environ.get('HAPISETUP_KIBANA_IMAGE_DIR_DEFAULT', str(Path('setup/docker_image/_kibana_default')))
environ['HAPISETUP_KIBANA_IMAGE_DIR'] = environ.get('HAPISETUP_KIBANA_IMAGE_DIR', environ['HAPISETUP_KIBANA_IMAGE_DIR_DEFAULT'])
environ['HAPISETUP_KIBANA_CONTAINER_DIR'] = environ.get('HAPISETUP_KIBANA_CONTAINER_DIR', str(Path('setup/docker_container/kibana')))
environ['HAPISETUP_KIBANA_PASSWORD'] = environ.get('HAPISETUP_KIBANA_PASSWORD', 'elastic')
environ['HAPISETUP_KIBANA_HOST'] = environ.get('HAPISETUP_KIBANA_HOST', '127.0.0.1')
environ['HAPISETUP_KIBANA_PORT'] = environ.get('HAPISETUP_KIBANA_PORT', '15601')
if not Path(environ['HAPISETUP_KIBANA_IMAGE_DIR']).is_dir():
    shutil.copytree(environ['HAPISETUP_KIBANA_IMAGE_DIR_DEFAULT'] , environ['HAPISETUP_KIBANA_IMAGE_DIR'])


environ['HAPISETUP_HAPI_IMAGE_DIR_DEFAULT'] = environ.get('HAPISETUP_HAPI_IMAGE_DIR_DEFAULT', str(Path('setup/docker_image/_hapi_default')))
environ['HAPISETUP_HAPI_IMAGE_DIR'] = environ.get('HAPISETUP_HAPI_IMAGE_DIR', environ['HAPISETUP_HAPI_IMAGE_DIR_DEFAULT'])
environ['HAPISETUP_HAPI_CONTAINER_DIR'] = environ.get('HAPISETUP_HAPI_CONTAINER_DIR', str(Path('hapi')))
environ['HAPISETUP_HAPI_HOST'] = environ.get('HAPISETUP_HAPI_HOST', '127.0.0.1')
environ['HAPISETUP_HAPI_PORT'] = environ.get('HAPISETUP_HAPI_PORT', '18080')
environ['HAPISETUP_HAPI_JAR'] = environ.get('HAPISETUP_HAPI_JAR', 'ROOT.war')

environ['HAPISETUP_HAPI_DB_HOST'] = environ.get('HAPISETUP_HAPI_DB_HOST', 'postgresql')
environ['HAPISETUP_HAPI_DB_PORT'] = environ.get('HAPISETUP_HAPI_DB_PORT', '5432')
environ['HAPISETUP_HAPI_DB_NAME'] = environ.get('HAPISETUP_HAPI_DB_NAME', 'postgress')
environ['HAPISETUP_HAPI_DB_USER'] = environ.get('HAPISETUP_HAPI_DB_USER', 'postgress')
environ['HAPISETUP_HAPI_DB_PASSWD'] = environ.get('HAPISETUP_HAPI_DB_PASSWD', 'postgress')

environ['HAPISETUP_HAPI_ES_HOST'] = environ.get('HAPISETUP_HAPI_ES_HOST', 'elasticsearch')
environ['HAPISETUP_HAPI_ES_PORT'] = environ.get('HAPISETUP_HAPI_ES_PORT', '9200')
environ['HAPISETUP_HAPI_ES_USER'] = environ.get('HAPISETUP_HAPI_ES_USER', 'elastic')
environ['HAPISETUP_HAPI_ES_PASSWD'] = environ.get('HAPISETUP_HAPI_ES_PASSWD', environ['HAPISETUP_ESREST_PASSWORD'])

environ['HAPISETUP_HAPI_CONFIG_LOCATIONS'] = environ.get('HAPISETUP_HAPI_CONFIG_LOCATIONS', 'classpath:application.yaml,file:./config/')
environ['HAPISETUP_HAPI_ARGS'] = environ.get(f'HAPISETUP_HAPI_ARGS', '--debug --spring.profiles.active={environ["HAPISETUP_PROFILES"]}')
environ['HAPISETUP_HAPI_API_URL'] = environ.get('HAPISETUP_HAPI_API_URL', f"http://{environ['HAPISETUP_HAPI_HOST']}:${environ['HAPISETUP_HAPI_PORT']}/fhir")

environ['HAPISETUP_HAPI_DEBUG_HOST'] = environ.get('HAPISETUP_HAPI_DEBUG_HOST', '127.0.0.1')
environ['HAPISETUP_HAPI_DEBUG_PORT'] = environ.get('HAPISETUP_HAPI_DEBUG_PORT', '18081')

environ['HAPISETUP_HAPI_JAVA_OPTIONS'] = environ.get('HAPISETUP_HAPI_JAVA_OPTIONS', '-Xmx4G -Dlogging.config=./config/logback-spring.xml ' +
                                                     f'')

if not Path(environ['HAPISETUP_HAPI_IMAGE_DIR']).is_dir():
    shutil.copytree(environ['HAPISETUP_HAPI_IMAGE_DIR_DEFAULT'] , environ['HAPISETUP_HAPI_IMAGE_DIR'])
(Path(environ['HAPISETUP_HAPI_CONTAINER_DIR'])).mkdir(parents=True, exist_ok=True)
