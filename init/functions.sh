#!/usr/bin/env bash

DOTFILE_HOME="$HOME/.dotfile"

function info() {
  echo -e "\e[0;36m $1 \e[0m"
}

function fail() {
  echo -e "\e[0;31m $1 \e[0m"
  exit
}

function get_file_by_os() {
	file=$1
	if [[ "$(cat /etc/issue 2> /dev/null)" =~ Ubuntu ]]; then
		ufile="$1_ubuntu"
		if [[ -f ufile ]]; then
			file=ufile
		fi
	fi

	if [[ "$OSTYPE" =~ ^darwin ]]; then
		ufile="$1_ubuntu"
		if [[ -f ufile ]]; then
			file=ufile
		fi
	fi
	return file
}