import os
import pathlib

# Allow a  "project" to set HS_PROFILES and other variables as needed and be committed.
init_project_path = pathlib.Path('env/project.py')
init_project_path.touch()
exec(open(init_project_path).read())

# Allow local configuration to set/override HS_PROFILES
init_local_path = pathlib.Path('env/local.py')
init_local_path.touch()
exec(open(init_local_path).read())

# If HS_PROFILES not already set, we set the default.
os.environ['HS_PROFILES'] = os.environ.get('HS_PROFILES', 'env-defaults,sb-defaults,sb-project,sb-local')

if os.environ['HS_PROFILES_PREFIX']:
    os.environ['HS_PROFILES'] = os.environ['HS_PROFILES_PREFIX'] + ',' + os.environ['HS_PROFILES']
if os.environ['HS_PROFILES_SUFFIX']:
    os.environ['HS_PROFILES'] = os.environ['HS_PROFILES'] + ',' + os.environ['HS_PROFILES_SUFFIX']

# Override with value from HS_PROFILES_CMDLINE which is set if --profiles command line option is used
# This is to help scripts set the profiles they want for that run of the script and overriding the above configuration.
os.environ['HS_PROFILES'] = os.environ.get('HS_PROFILES_CMDLINE', os.environ['HS_PROFILES'])

# Load the profiles
for env in [p.strip() for p in os.environ['HS_PROFILES'].split(',')]:
    if not env:
        continue
    if env.startswith('env-'):
        env_path = pathlib.Path(f'env/{env[4]}.py').absolute()
        print(f'Attempting to load environment file: {env_path}')
        exec(open(env_path).read())

# Create these files if needed so compose.yml can resolve them.
for service in ['postgresql', 'elasticsearch', 'kibana', 'hapi-build', 'hapi', 'janusgraph', 'cassandra']:
    pathlib.Path(f'service/{service}/local.env').touch()
