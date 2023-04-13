import os
import pathlib

os.environ['HS_PROFILES'] = os.environ.get('HS_PROFILES', 'env-defaults,hs-postgresql,hs-defaults,hs-local')

pathlib.Path('config/compose-postgresql-local.env').touch()
pathlib.Path('config/compose-elasticsearch-local.env').touch()
pathlib.Path('config/compose-kibana-local.env').touch()
pathlib.Path('config/compose-hapi-build-local.env').touch()
pathlib.Path('config/compose-hapi-local.env').touch()
