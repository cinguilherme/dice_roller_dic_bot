#!/bin/sh

echo "pre-commit run"

docker-compose run tests

exit $?