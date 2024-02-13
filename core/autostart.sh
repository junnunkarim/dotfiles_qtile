#!/bin/sh

run() {
  if ! pgrep -f "$1"; then
    "$@" &
  fi
}

run "/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1"
run "picom" -b
redshift -P -O 5500
run "greenclip" daemon
