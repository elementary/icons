#!/bin/sh

for s in 16 24 32 48 64 128; do

  cd status/$s || exit 1
  ln -s gpm-primary-000.svg          xfpm-primary-000.svg
  ln -s gpm-primary-020.svg          xfpm-primary-020.svg
  ln -s gpm-primary-040.svg          xfpm-primary-040.svg
  ln -s gpm-primary-060.svg          xfpm-primary-060.svg
  ln -s gpm-primary-080.svg          xfpm-primary-080.svg
  ln -s gpm-primary-100.svg          xfpm-primary-100.svg
  ln -s gpm-primary-000-charging.svg xfpm-primary-000-charging.svg
  ln -s gpm-primary-020-charging.svg xfpm-primary-020-charging.svg
  ln -s gpm-primary-040-charging.svg xfpm-primary-040-charging.svg
  ln -s gpm-primary-060-charging.svg xfpm-primary-060-charging.svg
  ln -s gpm-primary-080-charging.svg xfpm-primary-080-charging.svg
  ln -s gpm-primary-100-charging.svg xfpm-primary-100-charging.svg
  cd ../..
done
