from os import environ
from pathlib import Path

# Set this to a path to a Maven source folder to build the HAPI binary from
# This is mostly useful for development purposes. Others would point to the repo
# for this source. This setting overrides the configured repo.
environ['HS_HAPI_BUILD_SOURCE_PATH'] = \
    str(Path('/some/path/to/hapi/source'))

# https://oss.sonatype.org/content/repositories/snapshots/com/essaid/fhir/com.essaid.fhir.hapi-extensions/0.1.2-SNAPSHOT/com.essaid.fhir.hapi-extensions-0.1.2-20230110.071246-2-javadoc.jar.sha1
