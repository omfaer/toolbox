#!/usr/bin/python
# -*- coding: utf-8 -*-
# version:0.1.0 (sha3 denemek için yazılmış bir collector)
# Bu version yalnızca permission tabanlı hash çıkarıyor. pHash.

import xml.etree.ElementTree as ET
import sys
import getopt
import sqlite3 as sqlite
import time 
import sha3

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

    print "\n-------------------------PACKAGE-INFORMATIONS---------------------------------\n"
      
    if 'package' in root.attrib:
      print "package-name: ", root.attrib['package']
      print "\n----------USES-PERMISSIONS-------------\n"
      joinstr = root.attrib['package']
      for uses_permission in root.iter('uses-permission'):
        print uses_permission.attrib[namespace+'name']
        joinstr = joinstr + "||" + uses_permission.attrib[namespace+'name'] 
      
      print "\n************PERMISSIONS**************\n"
          
      for permission in root.iter('permission'):
        print permission.attrib[namespace+'name']
	joinstr = joinstr + "||" + permission.attrib[namespace+'name']
      print "-------------------------------------------------------------------------------------\n"   
      print joinstr
      print "-------------------------------------------------------------------------------------\n"   
      s=sha3.sha3_224(joinstr.encode('utf-8')).hexdigest()
      print(s)
      #print(s=='7369692ce85870d14bf72930dc2aa519ad5e0ca9ebc50509d9fa1fc7')
  except Exception as e:
    print ("\033[0;37;44m " + xml_file + "dosyasında hata \033[0;0;0m")
    with open("/home/omfaer/errors-encoder-collector.txt","a") as err:
      err.write("Hata veren dosya:" + xml_file +"\n")
      err.write("Verdiği hata:" + str(e) +"\n\n\n\n")
