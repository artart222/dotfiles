#!/usr/bin/bash

MODE=$(bsp-layout get $(bspc query -D -d focused --names))

if [[ $MODE == "tall" ]]; then
	bsp-layout set tailed $(bspc query -D -d focused --names)
	echo "is tall"
elif [[ $MODE == "tailed" ]]; then
	bsp-layout set monocle $(bspc query -D -d focused --names)
	echo "is tailed"
else
	bsp-layout set tall $(bspc query -D -d focused --names) --master-size .5
	echo "is mono"
fi
