#!/usr/bin/python
# -*- coding: utf-8 -*-
# version:0.1.0 (Sadece Hash Üretmek için.)

import xml.etree.ElementTree as ET
import sys
import getopt
import sqlite3 as sqlite
import time
import sha3

def get_hash(data):
  hdata = sha3.sha3_224(data.encode('utf-8')).hexdigest()
  return hdata

def show():
  for xml_file in sys.argv:
    if xml_file!=sys.argv[0]:
      try:
        manifest = ET.parse(xml_file)
        root = manifest.getroot()
        namespace = '{http://schemas.android.com/apk/res/android}'
        print ("\033[0;37;44m " + xml_file + "\033[0;0;0m")
        
        if 'package' in root.attrib:
          package_name = root.attrib['package']
          print "package-name: ", package_name

          phash_str = package_name       
          for uses_permission in root.iter('uses-permission'):
            phash_str = phash_str + "||" + uses_permission.attrib[namespace+'name'] 
 
          for permission in root.iter('permission'):
            phash_str = phash_str + "||" + permission.attrib[namespace+'name']
          
          psrhash_str = phash_str
          for service in root.iter('service'):
            psrhash_str = psrhash_str + "||" + service.attrib[namespace+'name'] 

          for receiver in root.iter('receiver'):
            psrhash_str = psrhash_str + "||" + receiver.attrib[namespace+'name'] 

          psr_hash = get_hash(psrhash_str)
          p_hash = get_hash(phash_str)

          print "  p_hash: ", p_hash 
          print "psr_hash: ", psr_hash

          print "\n----------USES-PERMISSIONS-------------\n"
          for uses_permission in root.iter('uses-permission'):
            print uses_permission.attrib[namespace+'name']

          print "\n************PERMISSIONS**************\n"      
          for permission in root.iter('permission'):
            print permission.attrib[namespace+'name']

          print "\n------------SERVICES-----------\n"
          for service in root.iter('service'):
            print service.attrib[namespace+'name'] 

          print "\n***********RECEIVERS**********\n"
          for receiver in root.iter('receiver'):
            print receiver.attrib[namespace+'name']

        else:
          print "Manifest dosyasında package bulunamadı."

      except Exception as e:
        print ("\033[0;37;44m " + xml_file + "dosyasında hata \033[0;0;0m")
        print ("\nVerdiği Hata: " + str(e) + "\n")
show()
