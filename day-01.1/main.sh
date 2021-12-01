#!/bin/sh

# Original solution:
# awk 'BEGIN {prev = 1000000000} {if ($1 > prev) {print}; prev = $1;}' | wc -l

awk 'NR == 1 {prev = $1} {if ($1 > prev) {print}; prev = $1;}' | wc -l
