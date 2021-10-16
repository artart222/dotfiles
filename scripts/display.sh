#!/usr/bin/bash

bspc monitor eDP-1 -d 1 2 3 4 5

MOT_STATE=$(xrandr | grep "HDMI-1" | grep "\bconnected\b")
if  [[ $MOT_STATE != "" ]]; then
	xrandr --output eDP-1 --mode 1920x1080 --rate 144\
		--output HDMI-1 --mode 1920x1080 --rate 144 --right-of eDP-1 --primary

	bspc monitor HDMI-1 -d 6 7 8 9 10
else

	xrandr --output eDP-1 --mode 1920x1080 --rate 60
	xrandr --output  HDMI-1  --off

	bspc monitor HDMI-1 -a 11

	bspc desktop -f 6
	bspc desktop -m eDP-1
	bspc desktop -f 7
	bspc desktop -m eDP-1
	bspc desktop -f 8
	bspc desktop -m eDP-1
	bspc desktop -f 9
	bspc desktop -m eDP-1
	bspc desktop -f 10
	bspc desktop -m eDP-1

	ANS=$(bspc query -T -m  | jshon -e desktops | grep name | awk '{print $2}'\
		| cut -c 2- | rev | cut  -c2- | rev | rev | cut -c2- | rev)
	if ! [[ $ANS =~ .*"6".* ]]; then
		bspc monitor eDP-1 -a 6
	fi

	ANS=$(bspc query -T -m  | jshon -e desktops | grep name | awk '{print $2}'\
		| cut -c 2- | rev | cut  -c2- | rev | rev | cut -c2- | rev)
	if ! [[ $ANS =~ .*"7".* ]]; then
		bspc monitor eDP-1 -a 7
	fi

	ANS=$(bspc query -T -m  | jshon -e desktops | grep name | awk '{print $2}'\
		| cut -c 2- | rev | cut  -c2- | rev | rev | cut -c2- | rev)
	if ! [[ $ANS =~ .*"8".* ]]; then
		bspc monitor eDP-1 -a 8
	fi

	ANS=$(bspc query -T -m  | jshon -e desktops | grep name | awk '{print $2}'\
		| cut -c 2- | rev | cut  -c2- | rev | rev | cut -c2- | rev)
	if ! [[ $ANS =~ .*"9".* ]]; then
		bspc monitor eDP-1 -a 9
	fi

	ANS=$(bspc query -T -m  | jshon -e desktops | grep name | awk '{print $2}'\
		| cut -c 2- | rev | cut  -c2- | rev | rev | cut -c2- | rev)
	if ! [[ $ANS =~ .*"10".* ]]; then
		bspc monitor eDP-1 -a 10
	fi


	bspc desktop -r 11
	bspc monitor -f HDMI-1
	bspc monitor -r

	bspc desktop -o 1 2 3 4 5 6 7 8 9 10
fi
