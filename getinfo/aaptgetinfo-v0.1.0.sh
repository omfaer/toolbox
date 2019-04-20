#!/bin/bash
# Apk Bilgilerin Almak İçin Gerekli Bash Script
# omfaer 25/03/2019
# version 0.1

for f in $@
do
aapt dump badging $f | grep -E 'uses-permission:|uses-feature:|package:' | awk '{print $1 $2}' | sed s/uses-permission:\name=/permission::/g | sed s/\'//g | sed s/package:name=/package::/ | sed s/uses-feature:name=/feature::/g | grep -v touchscreen >> info.txt 

aapt dump --values xmltree $f AndroidManifest.xml | grep -A 1 service | grep Raw: | awk '{print $3 $4}' | sed s/Raw:/service::/g | sed s/\(//g | sed s/\)//g | sed s/\"//g >> info.txt

aapt dump --values xmltree $f AndroidManifest.xml | grep -A 1 receiver | grep Raw: | awk '{print $3 $4}' | sed s/Raw:/receiver::/g | sed s/\(//g | sed s/\)//g | sed s/\"//g >> info.txt

echo "--------------------------------------------------------------------------------------------" >> info.txt
done 
