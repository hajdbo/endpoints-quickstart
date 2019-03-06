#!/bin/bash
# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set -euo pipefail

source util.sh

main() {
  # Get our working project, or exit if it's not set.
  local project_id=$(get_project_id)
  if [[ -z "$project_id" ]]; then
    exit 1
  fi
  # Because our included app uses query string parameters, we can include
  # them directly in the URL.
  #QUERY="curl \"https://${project_id}.appspot.com/airportName?iataCode=${DEVICESTR}\""
  QUERY="curl \"https://${project_id}.appspot.com/addDevice?deviceString=${DEVICESTR}\""
  # First, (maybe) print the command so the user can see what's being executed.
  if [[ "$QUIET" == "false" ]]; then
    echo "$QUERY"
  fi
  # Then actually execute it.
  # shellcheck disable=SC2086
  eval $QUERY
  # Our API doesn't print newlines. So we do it ourselves.
  printf '\n'
}

# Defaults.
#DEVICESTR="test1|MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE+IUEdJ2BfKXH/Jig+YZx3+xW3g2kG0R69Qeug1gOJbAW3LF5f7v8Nj1vc9UvOLXQ9cs3q+3pPlWqC0PTvS9UWg=="
DEVICESTR="test2|MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEEaPRph0eStiRZ7xbRvqTrcL7UEQMaYSICnw39RrvIL1DLg9rxNNMhRX8SvE/9bpuFqrV2U8iWxloqKqWWe/1Eg=="
QUIET="false"

if [[ "$#" == 0 ]]; then
  : # Use defaults.
elif [[ "$#" == 1 ]]; then
  DEVICESTR="$1"
elif [[ "$#" == 2 ]]; then
  # "Quiet mode" won't print the curl command.
  DEVICESTR="$1"
  QUIET="true"
else
  echo "Wrong number of arguments specified."
  echo "Usage: query_api.sh [iata-code] [quiet-mode]"
  exit 1
fi

main "$@"
