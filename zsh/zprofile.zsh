if [ -z "${DISPLAY}" ] && [ "${XDG_VTNR}" -eq 1 ]; then
  unset DISPLAY
  exec Hyprland
fi
