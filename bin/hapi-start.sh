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

. "${DIR}/.hapisetup"

echo "CWD: $(pwd)"
hapisetup --build-hapi --stdout --stderr --build-docker-image hapi start

#"${DIR}/hapi.sh" compose up --build --exit-code-from hapi  --abort-on-container-exit
