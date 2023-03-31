#!/bin/bash
# get the size of the the http response body
curl -s $1 | wc -c
