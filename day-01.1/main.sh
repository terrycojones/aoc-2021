#!/bin/sh

awk 'NR == 1 {prev = $1} {if ($1 > prev) {print}; prev = $1;}' | wc -l
