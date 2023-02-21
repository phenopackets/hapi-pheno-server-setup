from os import environ

# List profile names to load for environment loading and Spring Boot.
# "defaults" profile is needed unless you write a new one to cover all the needed default values/behavior
environ['HAPISETUP_PROFILES'] = environ.get('HAPISETUP_PROFILES', 'defaults,es,pg')
