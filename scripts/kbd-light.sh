#!/usr/bin/bash

get_current_light() {
	return $(cat /sys/class/leds/asus::kbd_backlight/brightness)
}

decrease_brightness() {
	if [[ "$((get_current_light))" > 0 ]]; then
		get_current_light
		echo "$(($? - 1))" > /sys/class/leds/asus::kbd_backlight/brightness
	fi
}

increase_brightness() {
	if [[ "$((get_current_light))" < 3 ]]; then
		get_current_light
		echo "$(($? + 1))" > /sys/class/leds/asus::kbd_backlight/brightness
	fi
}

if [[ $1 == "Down" ]]; then
	decrease_brightness
else
	increase_brightness
fi
