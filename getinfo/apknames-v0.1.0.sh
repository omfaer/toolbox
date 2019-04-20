#!/bin/bash
# Apk isimleri ve paket isimlerini almak için gerekli bash script
# omfaer 16/04/2019
# version 0.1.0

completed=0
for f in "$@"
do 
  #aapt dump badging "${f}"
  aapt dump badging "${f}" | grep "package: name=" | awk '{print $2}' | sed s/\'//g | sed s/name=// | tr -d '\n' >> namesapk.txt 

  echo ", ${f##*/}" >> namesapk.txt 

  let completed++
  echo "$completed.apk ${f}"

done
echo -e "\e[5m \e[46m $completed tanesi tamamlandı.\e[0m"
