#!/usr/bin/env bash
set -x
set -e
set -u
set -o pipefail
set -o noclobber
shopt -s nullglob

# stack overflow #59895
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do
  DIR="$(cd -P "$(dirname "$SOURCE")" && pwd)"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE"
done
DIR="$(cd -P "$(dirname "$SOURCE")" && pwd)"

HS_HOME=$(realpath "${DIR}/..")
export HS_HOME
cd "${HS_HOME}"

. "${HS_HOME}/bin/.hapisetup"

"${HS_HOME}/bin/hapi-stop.sh"

rm -rf "${HS_HOME}/hapi/target"
rm -rf "${HS_HOME}/setup/.venv"
rm -rf "${HS_HOME}/setup/docker_container/elasticsearch"
rm -rf "${HS_HOME}/setup/docker_container/postgresql"
rm -rf "${HS_HOME}/hapi/loaders/*/*loaded.txt"
rm -rf "${HS_HOME}/hapi/loaders/*/*loading.txt"