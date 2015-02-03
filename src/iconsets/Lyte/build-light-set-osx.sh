#!/usr/bin/env bash

for f in ./*.png ./*/*.png; do
    convert -negate $f
done