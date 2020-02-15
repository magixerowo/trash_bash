#!/bin/bash

for hosts in $(seq 0 255);do 
	for ports in $(ping -c 1 10.11.1.$hosts |grep "bytes from" |cut -d" " -f 4|cut -d":" -f1  &);do
		nmap -sC -sV $ports -oG ~/Desktop/msc/10.11.1.$hosts &
	done
done


