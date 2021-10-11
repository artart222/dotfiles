#!/usr/bin/bash

MOT_STATE=$(xrandr | grep "HDMI-1" | grep "\bconnected\b")
if  [[ $MOT_STATE != "" ]]; then
	xrandr --output eDP-1 --mode 1920x1080 --rate 144\
		--output HDMI-1 --mode 1920x1080 --rate 144 --right-of eDP-1 --primary

	bspc monitor eDP-1 -d 1 2 3 4 5
	bspc monitor HDMI-1 -d 6 7 8 9 10
else
	xrandr --output eDP-1 --mode 1920x1080 --rate 60

	bspc monitor HDMI-1 -a 11

	bspc  desktop -f 6
	bspc desktop -m eDP-1
	bspc  desktop -f 7
	bspc desktop -m eDP-1
	bspc  desktop -f 8
	bspc desktop -m eDP-1
	bspc  desktop -f 9
	bspc desktop -m eDP-1
	bspc  desktop -f 10
	bspc desktop -m eDP-1

	bspc desktop -r 11
	bspc monitor -r HDMI-1
	xrandr --output  HDMI-1  --off

	ANS=$(bspc query -T -m  | jshon -e desktops | grep name | awk '{print $2}'\
		| cut -c 2- | rev | cut  -c2- | rev | rev | cut -c2- | rev)
	if ! [[ $ANS =~ .*"1".* ]]; then
		bspc monitor eDP-1 -a 1
	fi

	ANS=$(bspc query -T -m  | jshon -e desktops | grep name | awk '{print $2}'\
		| cut -c 2- | rev | cut  -c2- | rev | rev | cut -c2- | rev)
	if ! [[ $ANS =~ .*"2".* ]]; then
		bspc monitor eDP-1 -a 2
	fi

	ANS=$(bspc query -T -m  | jshon -e desktops | grep name | awk '{print $2}'\
		| cut -c 2- | rev | cut  -c2- | rev | rev | cut -c2- | rev)
	if ! [[ $ANS =~ .*"3".* ]]; then
		bspc monitor eDP-1 -a 3
	fi

	ANS=$(bspc query -T -m  | jshon -e desktops | grep name | awk '{print $2}'\
		| cut -c 2- | rev | cut  -c2- | rev | rev | cut -c2- | rev)
	if ! [[ $ANS =~ .*"4".* ]]; then
		bspc monitor eDP-1 -a 4
	fi

	ANS=$(bspc query -T -m  | jshon -e desktops | grep name | awk '{print $2}'\
		| cut -c 2- | rev | cut  -c2- | rev | rev | cut -c2- | rev)
	if ! [[ $ANS =~ .*"5".* ]]; then
		bspc monitor eDP-1 -a 5
	fi

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


	bspc desktop -f 11
	bspc desktop -m eDP-1

	bspc monitor eDP-1 -o 1 2 3 4 5 6 7 8 9 10

	bspc desktop -f Desktop
	bspc desktop -r
fi
