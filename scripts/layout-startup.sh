#!/usr/bin/bash

# ANS=$(bspc query -T -m  | jshon -e desktops | grep name | awk '{print $2}'\
# 	| cut -c 2- | rev | cut -c2- | rev | rev | cut -c2- | rev)

for i in {1..10}; do
	bsp-layout set tall $i --master-size 0.5
done
