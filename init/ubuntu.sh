#!/usr/bin/env bash

set -e

echo ''

. ./functions.sh

for item in `ls $DOTFILE_HOME/link/`;do
  s="$DOTFILE_HOME/link/$item"
  t="$HOME/.`basename \"$item\"`"
  get_file_by_os s
  s=$?
  # ln -f -s $s $t
  info "link $s to $t"
done