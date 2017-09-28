
#!/bin/bash


if [[ $# == 0 ]]; then
	printf "Usage: %s FILE [NUM]\n" "$(basename "$0")"
	exit 1
else
	if [[ -f "$1" ]]; then
	if [[ $# > 1 ]]; then
		COUNTER=0
		while read -r LINE; do
			let COUNTER=$[$COUNTER+1]
			if [[ COUNTER -le $2 ]]; then
				printf "%s\n" "$LINE"

			else
				continue
			fi
		done < "$1"
	else
		COUNTER=0
		while read -r LINE; do
			let COUNTER=$[$COUNTER+1]
			if [[ COUNTER -le 3 ]]; then
				printf "%s\n" "$LINE"
			else
				continue
			fi
		done < "$1"
		fi
	else
		printf "\"%s\" is not a file\n" "$(basename "$1")"
		exit 1
	fi
fi

