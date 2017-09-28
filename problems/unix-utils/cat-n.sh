
#!/bin/bash

COUNTER=0
FILE=$1

if [[ $# -eq 0 ]]; then
        printf "Usage: %s file\n" "(basename "$0")"
        exit 1
else
        if [[ -f "$1" ]]; then
                i=0

                while read -r LINE; do
                        let ++i
                        printf "%1d %s\n" "$i" "$LINE"

                done < "$1"
        else

                printf "\"%s\" is not a file\n" "$(basename "$1")"
                exit 1
        fi
fi
