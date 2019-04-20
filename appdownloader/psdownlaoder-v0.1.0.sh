#!/bin/bash
# Emulator ile Play Store üzerinden Apk Yüklemek İçin Gerekli Bash Script
# omfaer 18/02/2019
# version 0.1.0

echo "İndirilenler Dizinindeki .apk uzantılı dosyalar siliniyor" 

adb shell rm -r sdcard/Download/*.apk

read -p "İndirilecek Paket Adını Giriniz:" package_name
echo $package_name

adb shell am start -a android.intent.action.VIEW -d 'market://details?id='$package_name

echo "İndirme linki açılıyor lütfen bekleyiniz.."
sleep 10

echo "İndirme Onaylanıyor"
adb shell input tap 900 550

echo "İndirme Onaylandı. Uygulama İndiriliyor.."

# dosya indirilirken boyutlar farklı olduğu için indirme süresi değişiyor bunun kontrolünü yapmak gerek
# chrome üzerinden bir dosya indirilirken isForeground=true oluyor. Ancak bu başka uygulamada kullanılan bir parametre de olabilir.
# adb shell dumpsys activity services | grep -i isForeground=true

sleep 5
echo "Uygulama Yükleniyor"
sleep 5
echo "Çıkış Yapılıyor.."


