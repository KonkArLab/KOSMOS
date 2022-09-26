#!/bin/bash
# recherche clef usb
# D. Hanon 7 novembre 2020

#recherche le nom de la clef
function find_USB
{
	if [ -z $1 ]; then
        echo
        exit -1
    fi
	clef=`ls $1`
	if [ $? != 0 ]; then
		echo $0 : ERREUR recherche clef
		exit -1
	fi
	clef=`echo $clef | cut -d" " -f1`
	if [ $? != 0 ]; then
		echo $0 : ERREUR recherche clef
		exit -1
	fi
	
	if [ -z $clef ]; then
        echo
        exit -1
	else
        echo -n $1/$clef
	fi
	
}
function find_USB_1
{
	ls /media/pi/ | { read a _; echo "$a"; }
}

find_USB $1
exit 0
