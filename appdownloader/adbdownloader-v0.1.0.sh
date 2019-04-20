#!/bin/bash
# Emulator ile adb üzerinden Apk Yüklemek İçin Gerekli Bash Script
# omfaer 18/02/2019
# version 0.1.0

echo "İndirilenler Dizinindeki .apk uzantılı dosyalar siliniyor" 

adb shell rm -r sdcard/Download/*.apk

read -p "İndirme Linkini Giriniz:" downloadURL
echo $downloadURL

# adb shell am start -a android.intent.action.VIEW -d $downloadURL && adb shell input keyevent 66 && adb shell input tap 890 1700
# adb shell pm install /storage/emulated/0/Download/WhatsApp_Messenger_v2.19.46_apkpure.com.apk

adb shell am start -a android.intent.action.VIEW -d $downloadURL

echo "İndirme linki açılıyor lütfen bekleyiniz.."
sleep 10

echo "İndirme Onaylanıyor"
adb shell input tap 890 1700

echo "İndirme Onaylandı. Dosya İndiriliyor.."

# dosya indirilirken boyutlar farklı olduğu için indirme süresi değişiyor bunun kontrolünü yapmak gerek
# chrome üzerinden bir dosya indirilirken isForeground=true oluyor. Ancak bu başka uygulamada kullanılan bir parametre de olabilir.
# adb shell dumpsys activity services | grep -i isForeground=true


sleep 15
echo "Uygulama Yükleniyor"
adb shell pm install /storage/emulated/0/Download/*.apk



