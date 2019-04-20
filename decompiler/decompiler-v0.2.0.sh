#!/bin/bash
# Apkları apktool ile decompile etmek İçin Gerekli Bash Script
# omfaer 15/04/2019
# version 0.2.0

completed=1
outsize=1
for f in $@
do
  let _status=(completed*100)/$#
 
  echo -e "\e[42m% [$_status] Apk: $f\e[0m"
  echo -e "\e[44mDecompile ediliyor...\e[0m"
  apktool d $f -o apkd$outsize
  echo -e "\e[44mDecompile edildi. Manifest dosyası alınıyor.\e[0m"
  cp /home/omfaer/sarge/apkd$outsize/AndroidManifest.xml /home/omfaer/sarge/apktoolmanifest/apkd$outsize.xml
  echo -e "\e[101mDizin siliniyor\e[0m"
  rm -rf /home/omfaer/sarge/apkd$outsize
  let outsize++
  let completed++
  echo -e "\e[93m--------------------------------------------------------------------------------------------\e[0m"
done
echo -e "\e[92mTüm işlemler tamamlandı\e[0m"



