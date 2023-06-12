import os

# Default profiles for the project
os.environ['HS_PROFILES'] = 'env-default,hapi-extensions,hs-default,hs-project,hs-local'

# Phenopackets uses this port offset
os.environ['HS_PORT_OFFSET'] = os.environ.get('HS_PORT_OFFSET', '30000')

os.environ['HS_HAPI_BUILD_GIT_REPO'] = os.environ.get('HS_HAPI_BUILD_GIT_REPO',
                                               'https://github.com/phenopackets/hapi-pheno-server.git')
os.environ['HS_HAPI_BUILD_GIT_REF'] = os.environ.get('HS_HAPI_BUILD_GIT_REF',
                                               'refs/remotes/origin/dev')
