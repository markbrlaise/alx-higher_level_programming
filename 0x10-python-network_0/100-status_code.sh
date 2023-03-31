#!/bin/bash
# display status code only from a response
curl -sI $1 | grep 'HTTP' | cut -d " " -f 2
