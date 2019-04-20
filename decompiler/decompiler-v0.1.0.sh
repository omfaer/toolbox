#!/bin/bash
# Apkları apktool ile decompile etmek İçin Gerekli Bash Script
# omfaer 04/04/2019
# version 0.1.0


for f in $@
do

 let _status=($f*100)/$#
 printf "\rProgress: $_status"
 #for i in $(seq 1 100)
 #do
 #    sleep 0.1 
 #    echo $i
 #done | whiptail --title 'APK-NAME:$f' --gauge 'Running...' 6 60 0

echo "APK-NAME:" $f
apktool d $f

echo "--------------------------------------------------------------------------------------------"
done



