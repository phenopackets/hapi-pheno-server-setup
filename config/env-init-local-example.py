from os import environ

# Set the following to your actual environment.
environ['HS_HAPI_HOST'] = '127.0.0.1'
environ['HS_HAPI_HOST_PUBLIC'] = '127.0.0.1'
environ['HS_HAPI_PORT'] = '18080'
environ['HS_HAPI_PORT_PUBLIC'] = '18080'

# Set your desired repo and build command like this:
environ['HS_HAPI_BUILD_GIT_REPO'] = 'https://github.com/hapifhir/hapi-fhir-jpaserver-starter.git'
environ['HS_HAPI_BUILD_GIT_REF'] = 'image/v6.4.0'
environ['HS_HAPI_BUILD_CMD'] = 'mvn -Pboot -DskipTests clean package'
