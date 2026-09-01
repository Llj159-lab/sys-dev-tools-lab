#!/usr/bin/env bash
if [ -f "$1" ]; then
    echo "file exists: $1"
else
    echo "file not found: $1"
fi
