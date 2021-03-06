#!/bin/bash

# standard sshd config path
SSHD_CONFIG=/etc/ssh/sshd_config

# helper functions
function tablize {
    awk '{printf(" | %-7s | %-7s | %-51s |\n", $1, $2, $3)}'
}
LINE=" +---------+---------+-----------------------------------------------------+"

# header
echo "$LINE"
echo "Cipher" "Algo" "Fingerprint" | tablize
echo "$LINE"

declare -A ALGOS
declare -a ASCII

# fingerprints
while read -r host_key; do
    cipher=$(echo "$host_key" | sed -r 's/^.*ssh_host_([^_]+)_key\.pub$/\1/'| tr 'a-z' 'A-Z')
    if [[ -f "$host_key" ]]; then
        if ssh-keygen -E md5 -l -f "$host_key" &>/dev/null; then
        IFS=$'\n'

        for algo in md5 sha256; do
            n=0
            for line in $(ssh-keygen -E $algo -lv -f "$host_key"); do
                n=$(( n + 1))
                if [[ $n -eq 1 ]]; then
                    ALGOS[$algo]=$(echo "$line" | awk '{print $2}')
                else
                    ASCII[$n]="${ASCII[$n]} ${line}"
                fi
            done
        done
        else
            ALGOS[md5]=$(ssh-keygen -l -f "$host_key" | awk '{print $2}')
            ALGOS[sha256]=$(awk '{print $2}' "$host_key" | base64 -d | sha256sum -b | awk '{print $1}' | xxd -r -p | base64)
        fi

        echo "$cipher" MD5 "${ALGOS[md5]}" | tablize
        echo "$cipher" SHA-256 "${ALGOS[sha256]}" | tablize
        echo "$LINE"
    fi
 done < <(awk '/^HostKey/ {sub(/^HostKey\s+/,"");print $0".pub"};' $SSHD_CONFIG)

echo
for line in "${ASCII[@]}"; do
    echo "$line"
done
