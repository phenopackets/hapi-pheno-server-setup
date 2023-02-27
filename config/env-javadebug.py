from os import environ

environ['HAPISETUP_HAPI_JAVA_OPTIONS'] = \
    environ['HAPISETUP_HAPI_JAVA_OPTIONS'] + \
    f' -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=localhost:8081'
