#!/usr/bin/env bash
#set -x
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
HAPISETUP_HOME=$(realpath "${DIR}/..")
cd "${HAPISETUP_HOME}"

export HAPISETUP_HOME
export HAPISETUP_VENV="${HAPISETUP_VENV:-"${HAPISETUP_HOME}/setup/.venv"}"

if [[ ! -d ${HAPISETUP_VENV} ]]; then
  python3 -m venv --copies "${HAPISETUP_VENV}"
  . "${HAPISETUP_VENV}/bin/activate"
  pip install -U pip
  pip install -e "${HAPISETUP_HOME}/setup/cli"
else
  . "${HAPISETUP_VENV}/bin/activate"
fi

#export HAPISETUP_HAPI_ARGS="--debug --spring.profiles.active=pg,es,debug"

hapisetup "$@"
