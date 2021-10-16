if [[ $(xrandr | grep "HDMI-1 connected") ]]; then
	export TRAY1=none
	export TRAY2=right
else
	export TRAY1=right
fi
