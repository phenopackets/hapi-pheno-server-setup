from os import environ

environ['HS_PROFILES'] = environ.get('HS_PROFILES', 'env-defaults,hs-defaults,hs-postgresql,hs-local')

