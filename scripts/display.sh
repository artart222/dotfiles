#!/usr/bin/bash

MOT_STATE=$(xrandr | grep "HDMI-A-0" | grep "\bconnected\b")
if  [[ $MOT_STATE != "" ]]; then
	xrandr --output eDP --mode 1920x1080 --rate 144\
		--output HDMI-A-0 --mode 1920x1080 --rate 144 --right-of eDP --primary

	bspc monitor eDP -d 1 2 3 4 5
	bspc monitor HDMI-A-0 -d 6 7 8 9 10
else
	xrandr --output eDP --mode 1920x1080 --rate 60

	bspc monitor HDMI-A-0 -a 11

	bspc  desktop -f 6
	bspc desktop -m eDP
	bspc  desktop -f 7
	bspc desktop -m eDP
	bspc  desktop -f 8
	bspc desktop -m eDP
	bspc  desktop -f 9
	bspc desktop -m eDP
	bspc  desktop -f 10
	bspc desktop -m eDP

	bspc desktop -r 11
	bspc monitor -r HDMI-A-0
	xrandr --output  HDMI-A-0  --off

	ANS=$(bspc query -T -m  | jshon -e desktops | grep name | awk '{print $2}'\
		| cut -c 2- | rev | cut  -c2- | rev | rev | cut -c2- | rev)
	if ! [[ $ANS =~ .*"1".* ]]; then
		bspc monitor eDP -a 1
	fi

	ANS=$(bspc query -T -m  | jshon -e desktops | grep name | awk '{print $2}'\
		| cut -c 2- | rev | cut  -c2- | rev | rev | cut -c2- | rev)
	if ! [[ $ANS =~ .*"2".* ]]; then
		bspc monitor eDP -a 2
	fi

	ANS=$(bspc query -T -m  | jshon -e desktops | grep name | awk '{print $2}'\
		| cut -c 2- | rev | cut  -c2- | rev | rev | cut -c2- | rev)
	if ! [[ $ANS =~ .*"3".* ]]; then
		bspc monitor eDP -a 3
	fi

	ANS=$(bspc query -T -m  | jshon -e desktops | grep name | awk '{print $2}'\
		| cut -c 2- | rev | cut  -c2- | rev | rev | cut -c2- | rev)
	if ! [[ $ANS =~ .*"4".* ]]; then
		bspc monitor eDP -a 4
	fi

	ANS=$(bspc query -T -m  | jshon -e desktops | grep name | awk '{print $2}'\
		| cut -c 2- | rev | cut  -c2- | rev | rev | cut -c2- | rev)
	if ! [[ $ANS =~ .*"5".* ]]; then
		bspc monitor eDP -a 5
	fi

	ANS=$(bspc query -T -m  | jshon -e desktops | grep name | awk '{print $2}'\
		| cut -c 2- | rev | cut  -c2- | rev | rev | cut -c2- | rev)
	if ! [[ $ANS =~ .*"6".* ]]; then
		bspc monitor eDP -a 6
	fi

	ANS=$(bspc query -T -m  | jshon -e desktops | grep name | awk '{print $2}'\
		| cut -c 2- | rev | cut  -c2- | rev | rev | cut -c2- | rev)
	if ! [[ $ANS =~ .*"7".* ]]; then
		bspc monitor eDP -a 7
	fi

	ANS=$(bspc query -T -m  | jshon -e desktops | grep name | awk '{print $2}'\
		| cut -c 2- | rev | cut  -c2- | rev | rev | cut -c2- | rev)
	if ! [[ $ANS =~ .*"8".* ]]; then
		bspc monitor eDP -a 8
	fi

	ANS=$(bspc query -T -m  | jshon -e desktops | grep name | awk '{print $2}'\
		| cut -c 2- | rev | cut  -c2- | rev | rev | cut -c2- | rev)
	if ! [[ $ANS =~ .*"9".* ]]; then
		bspc monitor eDP -a 9
	fi


	bspc desktop -f 11
	bspc desktop -m eDP

	bspc monitor eDP -o 1 2 3 4 5 6 7 8 9 10

	bspc desktop -f Desktop
	bspc desktop -r
fi
