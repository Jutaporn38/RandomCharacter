#!/bin/bash

random_color() {
  echo $((RANDOM % 8 + 30))
}

random_text() {
  tr -dc 'A-Za-z0-9' </dev/urandom | head -c$(($RANDOM % 80 + 20))
}

clear
while true; do
  for i in {1..20}; do
    color=$(random_color)
    text=$(random_text)
    echo -e "\033[${color}m${text}\033[0m"
  done
done
