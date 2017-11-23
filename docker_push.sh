#!/usr/bin/env bash
docker build -t base -f Dockerfile.base .
docker tag base sejun/base
docker push sejun/base