#!/bin/bash
#post json data (we need a content header then)
curl -X POST -s -H "Content-Type: application/json" -d "$(cat $2)" $1
