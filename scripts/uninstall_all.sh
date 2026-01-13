#!/bin/bash

# collect all installed packages
PACKAGES=$(pip freeze | grep -v "^-e" | sed 's/@.*//' | sed 's/\=\=.*//')
# uninstall packages without exiting on a failure 
for package in $PACKAGES; do
  pip uninstall -y $package
done
