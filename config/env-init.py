from os import environ

environ['HS_PROFILES'] = environ.get('HS_PROFILES', 'env-defaults,hs-defaults,hs-pg,hs-es,hs-local')

# These can be overridden in an env-init-local.py if needed to make HAPI happy with its URL.
# Copy env-init-local-example.py and adjust as needed.
environ['HS_HAPI_HOST'] = environ.get('HS_HAPI_HOST', '127.0.0.1')
environ['HS_HAPI_HOST_PUBLIC'] = environ.get('HS_HAPI_HOST_PUBLIC', '127.0.0.1')
environ['HS_HAPI_PORT'] = environ.get('HS_HAPI_PORT', '18080')
environ['HS_HAPI_PORT_PUBLIC'] = environ.get('HS_HAPI_PORT_PUBLIC', '18080')
