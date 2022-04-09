# Find number of monitors
MONITORS_NUM=$(xrandr | grep "\bconnected" | wc -l)
AC_ADAPTER=$(acpi -a | cut -d' ' -f3 | cut -d- -f1)

# This block will configure monitors. This will turn on and off extra monitors
# And it will set refresh rate of monitor based on AC adapter status. If laptop
# is connected to power source it will
# set monitors refresh rate to 144 else to 60
if [[ $MONITORS_NUM == "1" ]]; then
  if [[ $AC_ADAPTER == "on" ]]; then
    xrandr --output eDP-1 --mode 1920x1080 --rate 144 \
      | xrandr --output HDMI-1 --off
  else
    xrandr --output eDP-1 --mode 1920x1080 --rate 60 \
      | xrandr --output HDMI-1 --off
  fi
elif [[ $MONITORS_NUM == "2" ]]; then
  if [[ $AC_ADAPTER == "on" ]]; then
    xrandr --output eDP-1 --mode 1920x1080 --rate 144 \
      | xrandr --output HDMI-1 --mode 1920x1080 --rate 144 --right-of eDP-1 --primary
  else
    xrandr --output eDP-1 --mode 1920x1080 --rate 60 \
      | xrandr --output HDMI-1 --mode 1920x1080 --rate 60 --right-of eDP-1 --primary
  fi
fi
