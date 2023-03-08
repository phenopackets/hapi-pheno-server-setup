import os
import shutil
from os import environ
from pathlib import Path

environ['HS_UID'] = environ.get('HS_UID', str(os.getuid()))
environ['HS_GID'] = environ.get('HS_GID', str(os.getgid()))

#  Postgresql =====================

environ['HS_PG_IMAGE_DIR_DEFAULT'] = environ.get('HS_PG_IMAGE_DIR_DEFAULT',
                                                 str(Path('setup/docker_image/_postgresql_default')))
environ['HS_PG_IMAGE_DIR'] = environ.get('HS_PG_IMAGE_DIR', environ['HS_PG_IMAGE_DIR_DEFAULT'])
environ['HS_PG_CONTAINER_DIR'] = environ.get('HS_PG_CONTAINER_DIR',
                                             str(Path('setup/docker_container/postgresql')))
environ['HS_PG_PASSWORD'] = environ.get('HS_PG_PASSWORD', 'postgres')
environ['HS_PG_HOST'] = environ.get('HS_PG_HOST', '127.0.0.1')
environ['HS_PG_PORT'] = environ.get('HS_PG_PORT', '15432')

if not Path(environ['HS_PG_IMAGE_DIR']).is_dir():
    shutil.copytree(environ['HS_PG_IMAGE_DIR_DEFAULT'], environ['HS_PG_IMAGE_DIR'])
(Path(environ['HS_PG_CONTAINER_DIR']) / 'data-volume').mkdir(parents=True, exist_ok=True)

#  Elasticsearch ========================

environ['HS_ESREST_IMAGE_DIR_DEFAULT'] = environ.get('HS_ESREST_IMAGE_DIR_DEFAULT',
                                                     str(Path('setup/docker_image/_elasticsearch_default')))
environ['HS_ESREST_IMAGE_DIR'] = environ.get('HS_ESREST_IMAGE_DIR',
                                             environ['HS_ESREST_IMAGE_DIR_DEFAULT'])
environ['HS_ESREST_CONTAINER_DIR'] = environ.get('HS_ESREST_CONTAINER_DIR',
                                                 str(Path('setup/docker_container/elasticsearch')))
environ['HS_ESREST_PASSWORD'] = environ.get('HS_ESREST_PASSWORD', 'elastic')
environ['HS_ESREST_HOST'] = environ.get('HS_ESREST_HOST', '127.0.0.1')
environ['HS_ESREST_PORT'] = environ.get('HS_ESREST_PORT', '19200')
if not Path(environ['HS_ESREST_IMAGE_DIR']).is_dir():
    shutil.copytree(environ['HS_ESREST_IMAGE_DIR_DEFAULT'], environ['HS_ESREST_IMAGE_DIR'])
(Path(environ['HS_ESREST_CONTAINER_DIR']) / 'data-volume').mkdir(parents=True, exist_ok=True)

# Kibana  ============================

environ['HS_KIBANA_IMAGE_DIR_DEFAULT'] = environ.get('HS_KIBANA_IMAGE_DIR_DEFAULT',
                                                     str(Path('setup/docker_image/_kibana_default')))
environ['HS_KIBANA_IMAGE_DIR'] = environ.get('HS_KIBANA_IMAGE_DIR',
                                             environ['HS_KIBANA_IMAGE_DIR_DEFAULT'])
environ['HS_KIBANA_CONTAINER_DIR'] = environ.get('HS_KIBANA_CONTAINER_DIR',
                                                 str(Path('setup/docker_container/kibana')))
environ['HS_KIBANA_PASSWORD'] = environ.get('HS_KIBANA_PASSWORD', 'elastic')
environ['HS_KIBANA_HOST'] = environ.get('HS_KIBANA_HOST', '127.0.0.1')
environ['HS_KIBANA_PORT'] = environ.get('HS_KIBANA_PORT', '15601')
if not Path(environ['HS_KIBANA_IMAGE_DIR']).is_dir():
    shutil.copytree(environ['HS_KIBANA_IMAGE_DIR_DEFAULT'], environ['HS_KIBANA_IMAGE_DIR'])

# ========================================
# HAPI build  ============================
# ========================================

environ['HS_HAPI_BUILD_IMAGE_DIR_DEFAULT'] = environ.get('HS_HAPI_BUILD_IMAGE_DIR_DEFAULT',
                                                         str(Path('setup/docker_image/_hapi_build_default')))
environ['HS_HAPI_BUILD_IMAGE_DIR'] = environ.get('HS_HAPI_BUILD_IMAGE_DIR',
                                                 environ['HS_HAPI_BUILD_IMAGE_DIR_DEFAULT'])
environ['HS_HAPI_BUILD_CONTAINER_DIR'] = environ.get('HS_HAPI_BUILD_CONTAINER_DIR',
                                                     str(Path('setup/docker_container/hapi_build')))

# types: no, download, maven, git
environ['HS_HAPI_BUILD_TYPE'] = environ.get('HS_HAPI_BUILD_TYPE', 'git')

# type download
environ['HS_HAPI_BUILD_DOWNLOAD_URL'] = environ.get('HS_HAPI_BUILD_DOWNLOAD_URL', '')

# type git
environ['HS_HAPI_BUILD_GIT_REPO'] = environ.get('HS_HAPI_BUILD_GIT_REPO',
                                                'https://github.com/hapifhir/hapi-fhir-jpaserver-starter.git')
environ['HS_HAPI_BUILD_GIT_REF'] = environ.get('HS_HAPI_BUILD_GIT_REF',
                                               'refs/tags/v6.4.0')

# type source
environ['HS_HAPI_BUILD_SOURCE_PATH'] = environ.get('HS_HAPI_BUILD_SOURCE_PATH', '')
environ['HS_HAPI_BUILD_VOLUME'] = environ.get('HS_HAPI_BUILD_VOLUME',
                                              environ['HS_HAPI_BUILD_SOURCE_PATH']
                                              or str(Path(environ[
                                                              'HS_HAPI_BUILD_CONTAINER_DIR']) / 'data-volume'))
environ['HS_HAPI_BUILD_CMD'] = environ.get('HS_HAPI_BUILD_CMD',
                                           'mvn -Pboot -DskipTests clean package')
environ['HS_HAPI_BUILD_ALWAYS'] = environ.get('HS_HAPI_BUILD_ALWAYS', 'false')

if not Path(environ['HS_HAPI_BUILD_IMAGE_DIR']).is_dir():
    shutil.copytree(environ['HS_HAPI_BUILD_IMAGE_DIR_DEFAULT'], environ['HS_HAPI_BUILD_IMAGE_DIR'])
(Path(environ['HS_HAPI_BUILD_CONTAINER_DIR']) / 'data-volume').mkdir(parents=True, exist_ok=True)

# HAPI  ======================

environ['HS_HAPI_VERSION'] = environ.get('HS_HAPI_VERSION',
                                         '6.4.0')

environ['HS_HAPI_IMAGE_DIR_DEFAULT'] = environ.get('HS_HAPI_IMAGE_DIR_DEFAULT',
                                                   str(Path('setup/docker_image/_hapi_default')))
environ['HS_HAPI_IMAGE_DIR'] = environ.get('HS_HAPI_IMAGE_DIR',
                                           environ['HS_HAPI_IMAGE_DIR_DEFAULT'])
environ['HS_HAPI_CONTAINER_DIR'] = environ.get('HS_HAPI_CONTAINER_DIR',
                                               'hapi')
environ['HS_HAPI_HOST'] = environ.get('HS_HAPI_HOST',
                                      '127.0.0.1')
environ['HS_HAPI_HOST_PUBLIC'] = environ.get('HS_HAPI_HOST_PUBLIC',
                                             '127.0.0.1')
environ['HS_HAPI_PORT'] = environ.get('HS_HAPI_PORT',
                                      '18080')
environ['HS_HAPI_PORT_PUBLIC'] = environ.get('HS_HAPI_PORT_PUBLIC',
                                      '18080')

environ['HS_HAPI_DB_HOST'] = environ.get('HS_HAPI_DB_HOST',
                                         'postgresql')
environ['HS_HAPI_DB_PORT'] = environ.get('HS_HAPI_DB_PORT',
                                         '5432')
environ['HS_HAPI_DB_NAME'] = environ.get('HS_HAPI_DB_NAME',
                                         'postgres')
environ['HS_HAPI_DB_USER'] = environ.get('HS_HAPI_DB_USER',
                                         'postgres')
environ['HS_HAPI_DB_PASSWD'] = environ.get('HS_HAPI_DB_PASSWD',
                                           'postgres')

environ['HS_HAPI_ES_HOST'] = environ.get('HS_HAPI_ES_HOST',
                                         'elasticsearch')
environ['HS_HAPI_ES_PORT'] = environ.get('HS_HAPI_ES_PORT',
                                         '9200')
environ['HS_HAPI_ES_USER'] = environ.get('HS_HAPI_ES_USER',
                                         'elastic')
environ['HS_HAPI_ES_PASSWD'] = environ.get('HS_HAPI_ES_PASSWD',
                                           environ['HS_ESREST_PASSWORD'])

environ['HS_HAPI_CONFIG_LOCATIONS'] = environ.get('HS_HAPI_CONFIG_LOCATIONS',
                                                  'file:./config/,classpath:application.yaml')
environ['HS_HAPI_API_URL'] = environ.get('HS_HAPI_API_URL',
                                         f"http://{environ['HS_HAPI_HOST_PUBLIC']}:{environ['HS_HAPI_PORT_PUBLIC']}/fhir")

environ['HS_HAPI_DEBUG_HOST'] = environ.get('HS_HAPI_DEBUG_HOST',
                                            '127.0.0.1')
environ['HS_HAPI_DEBUG_PORT'] = environ.get('HS_HAPI_DEBUG_PORT',
                                            '18081')

# this is what HAPI is launched with
environ['HS_HAPI_JAVA_OPTIONS'] = environ.get('HS_HAPI_JAVA_OPTIONS',
                                              '-Xmx4G -Dlogging.config=./config/logback-spring.xml ' +
                                              f'-Dspring.config.location={environ["HS_HAPI_CONFIG_LOCATIONS"]} ')
environ['HS_HAPI_JAR'] = environ.get('HS_HAPI_JAR',
                                     'ROOT.war')
environ['HS_HAPI_ARGS'] = environ.get(f'HS_HAPI_ARGS',
                                      f'--debug --spring.profiles.active={environ["HS_PROFILES"]}')

if not Path(environ['HS_HAPI_IMAGE_DIR']).is_dir():
    shutil.copytree(environ['HS_HAPI_IMAGE_DIR_DEFAULT'], environ['HS_HAPI_IMAGE_DIR'])
(Path(environ['HS_HAPI_CONTAINER_DIR'])).mkdir(parents=True, exist_ok=True)
