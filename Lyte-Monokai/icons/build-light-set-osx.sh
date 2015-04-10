#!/usr/bin/env bash

rm -r ../Lyte-Light
mkdir ../Lyte-Light/
mkdir ../Lyte-Light/spinner
mkdir ../Lyte-Light/gui
mkdir ../Lyte-Light/panel

for f in ./*.png ./*/*.png; do
    convert "$f" -negate "../Lyte-Light/$f"
done