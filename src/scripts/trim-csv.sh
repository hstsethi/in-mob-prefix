#!/bin/sh

# Part of  In Mob Prefix project by hstsethi <hstsethi@outlook.com>

# This is a very simple script to remove excessive columns from CSV. For our use case, only 3 columns are required, so we will remove any other

# The cut based solution is way faster, cross-platform than Awk, Python

if [ $# -eq 0 ]; then
    echo "Usage: sh trim-csv.sh <input_filename> <output_filename>"
    exit 1
fi

cut --fields=2 $1 > $2
