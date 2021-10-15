#!/usr/bin/bash

for i in {1..10}; do
	bsp-layout set tall $i --master-size 0.5
done
