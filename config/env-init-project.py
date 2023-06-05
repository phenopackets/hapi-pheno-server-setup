# Use this file to set project specific settings
# "project" here means a fork of the upstream ShahimEssaid/hapi-compose-setup for a use by a project
# This file should focus on setting HS_PROFILES and other variables to values needed by all the "run instances"
# of the project.
# A local "run" of the project can further override the settings for the local "instance" in env-init-local.py
# to set instance specific values.

# See config/env-init-local-example.py for possible values to set here or in the local file.
# The full list of environment variables is in config/env-defaults.py.

import os

# Phenopackets uses this port offset
os.environ['HS_PORT_OFFSET'] = os.environ.get('HS_PORT_OFFSET', '30000')

os.environ['HS_HAPI_BUILD_GIT_REPO'] = os.environ.get('HS_HAPI_BUILD_GIT_REPO',
                                               'https://github.com/phenopackets/hapi-pheno-server.git')
os.environ['HS_HAPI_BUILD_GIT_REF'] = os.environ.get('HS_HAPI_BUILD_GIT_REF',
                                               'refs/remotes/origin/dev')