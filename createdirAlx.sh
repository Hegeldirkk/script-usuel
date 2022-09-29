#!/usr/bin/env bash
if [ -n "$1" ]
then
	echo "$1"
	mkdir "$1" && cd "$1" || exit
	if [[ -z "$2" ]]
	then
		echo "USAGE: ./createdirAlx.sh FILE_NAME TITLE"
		echo "Enter a Title"
		read -r title
		echo "# $title" > README.md
	else
		echo "# $1" > README.md
	fi
else
	echo "USAGE: ./createdirAlx.sh FILE_NAME TITLE"
fi
