#!/usr/bin/env bash

# This script is intended to be executed by Jenkins.

# Bail on first error.
set -e

S=$(basename $0)

echo -e "\n$S: Cleaning out any previous build artifacts..."
if [ -f Makefile ]; then 
	make distclean 
fi

echo -e "\n$S: Building project..."
# If you need to compile stuff for your project, do it here
# qmake
# make

echo -e "\n$S: Creating debian package..."
cd debian
make clean
make

echo -e "\n$S: Success!\n"


