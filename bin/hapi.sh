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

HS_HOME=$(realpath "${DIR}/..")
export HS_HOME
cd "${HS_HOME}"


# https://stackoverflow.com/questions/5947742/how-to-change-the-output-color-of-echo-in-linux
#Black        0;30     Dark Gray     1;30
#Red          0;31     Light Red     1;31
#Green        0;32     Light Green   1;32
#Brown/Orange 0;33     Yellow        1;33
#Blue         0;34     Light Blue    1;34
#Purple       0;35     Light Purple  1;35
#Cyan         0;36     Light Cyan    1;36
#Light Gray   0;37     White         1;37
export YELLOW='\033[0;33m'
export RED='\033[0;31m'
export GREEN='\033[0;32m'
export NO_COLOR='\033[0m'

function  loginfo() {
  echo -e "${GREEN}INFO : $1${NO_COLOR}"
}
#export -f loginfo

function  logwarn() {
  echo -e "${YELLOW}WARN : $1${NO_COLOR}"
}
#export -f logwarn

function  logerror() {
  echo -e "${RED}ERROR: $1${NO_COLOR}"
}
#export -f logerror


# OpenSearch warn if swap is on
#
# TODO: fix this for macOS (does not have free)
#if free | awk '/^Swap:/ {exit !$2}'; then
#    logwarn "swap is on but OpenSearch recommends it off: https://opensearch.org/docs/latest/install-and-configure/install-opensearch/docker/#important-host-settings"
#fi

# OpenSearch error and exit if memory maps lower than recommended.
# TODO: check if and how to do this in macOS
#read -r mem_maps < /proc/sys/vm/max_map_count
#if [[ ${mem_maps} -lt 262144 ]]; then
#    logerror "memory maps value is ${mem_maps}"
#    logerror "memory maps is less than what OpenSearch recommends: https://opensearch.org/docs/latest/install-and-configure/install-opensearch/docker/#important-host-settings"
#    logerror "exiting 10"
#    exit 10
#fi


export HS_VENV="${HS_VENV:-"${HS_HOME}/setup/.venv"}"

if [[ ! -d ${HS_VENV} ]]; then
  # TODO: fix the --copies issue with some/all macOS
  python3 -m venv "${HS_VENV}"
  . "${HS_VENV}/bin/activate"
  pip install -U pip
  pip install -e "${HS_HOME}/setup/cli"
else
  . "${HS_VENV}/bin/activate"
fi

hapi "$@"
