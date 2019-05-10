#!/usr/bin/python
# -*- coding: utf-8 -*-
# version:0.1.0 (xml uzantılı dosyalara paket ismini yazdırmak için.)
# Eğer birden fazla aynı paket ismine sahip dosya varsa pas geçiyor

import xml.etree.ElementTree as ET
import sys
import getopt
import time
import os

args_number=0
for xml_file in sys.argv:
  args_number += 1
  if args_number % 100 == 0:
    time.sleep(5)
  if xml_file!=sys.argv[0]:
    try:
      manifest = ET.parse(xml_file)
      root = manifest.getroot()
      namespace = '{http://schemas.android.com/apk/res/android}'
      print ("\033[0;37;44m " + xml_file + "\033[0;0;0m")
      category = xml_file.split("/")[-2]
      print "Dizin Adı/Kategori: " + category
      print "Dosya Adı: " + xml_file

      abspath = os.path.abspath(xml_file)
      print "Tam Dosya Yolu: " + abspath

      dirname = os.path.dirname(xml_file)
      splitpath = os.path.abspath(dirname)+"/"
      print "Dosya Yolu: " + splitpath
      
      if 'package' in root.attrib:
        print "package-name: ", root.attrib['package']
        new_name = splitpath+root.attrib['package']+".xml"
        exists = os.path.isfile(new_name)
        if exists:
          print new_name + " isminde bir dosya zaten var. " + abspath + " isimlendirmesi yapılamadı."
        else:
          os.rename(xml_file, new_name)
          print xml_file + " dosya ismi " + new_name +" olarak değiştirildi."
        
    except Exception as e:
      with open("/home/omfaer/errors-renamer.txt","a") as err:
        err.write("Hata veren dosya:" + xml_file +"\n")
        err.write("Verdiği hata: " + str(e) +"\n\n\n\n")
        print "Hata! " + xml_file + "dosyası hataya yol açtı."
        print "Hata Mesajı: "+ str(e)
