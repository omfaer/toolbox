#!/bin/bash
# Apkları apktool ile decompile etmek İçin Gerekli Bash Script
# omfaer 15/04/2019
# version 0.3.0

exec 2> >(tee aerror.txt)
#trap 'exec 2>&4 1>&3' 0 1 2 3
#exec 1>alog.txt 2>&1
#echo "$(date) : part 1 - start" >&3

completed=1
outsize=1
for f in "$@"
do
let _status=(completed*100)/$#
  echo -e "\e[42m% [$_status] Apk: $f\e[0m"
  echo -e "\e[44mDecompile ediliyor...\e[5m \e[46m $outsize.apk \e[0m"
  sudo apktool d "$f" -o apkd$outsize
  echo -e "\e[44mDecompile edildi. Manifest dosyası alınıyor.\e[0m" 
  cp /home/omfaer/apkd$outsize/AndroidManifest.xml /home/omfaer/apktoolmanifest/apkd$outsize.xml 
  echo -e "\e[101mDizin siliniyor\e[0m"
  rm -rf /home/omfaer/apkd$outsize
  let outsize++
  let completed++
  echo -e "\e[93m--------------------------------------------------------------------------------------------\e[0m"
done
echo -e "\e[92mTüm işlemler tamamlandı\e[0m"
