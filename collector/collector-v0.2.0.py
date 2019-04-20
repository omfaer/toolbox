#!/usr/bin/python
# -*- coding: utf-8 -*-
# version:0.2.0 (dosyaya yazdırma)

import xml.etree.ElementTree as ET
import sys
import getopt

#manifest = ET.parse("/home/omfaer/apktool_decompile/lastpass/AndroidManifest.xml")

with open("/home/omfaer/desktop/info_apk.txt","a") as dosya:
  for xml_file in sys.argv:
   if xml_file!=sys.argv[0]:
    manifest = ET.parse(xml_file)
    root = manifest.getroot()
    namespace = '{http://schemas.android.com/apk/res/android}'
    # note = "Güncellenmiş Uygulamaları takip edebilmek adına version bilgisi vs tutmak hatta buna göre sorgulamak gerekebilir."
    
    #print "root tag: ", root.tag
    
    #print "root attrib: ", root.attrib
    
    print "\n-------------------------PACKAGE-INFORMATİONS---------------------------------\n"
    
    if 'package' in root.attrib:
      print "package-name: ", root.attrib['package']
      dosya.write("package-name: " + root.attrib['package'] + "\n" )
    else:
      print "Paket adı bulunamadı"
    
    if 'platformBuildVersionName' in root.attrib:
      print "version-name: ", root.attrib['platformBuildVersionName']
      dosya.write("version-name: " +  root.attrib['platformBuildVersionName'] + "\n")
    else:
      print "Version Name bulunamadı"
    
    if 'platformBuildVersionCode' in root.attrib:
      print "version-code: ", root.attrib['platformBuildVersionCode']
    else:
      print "Version Code bulunamadı"
    
    #print "--------------------------------------------------------------------------\n\n"
    
    #for child in root:
    #    print(child.tag, child.attrib)
    
    #print "\n-----------------------------META-DATA------------------------------------\n"
    #
    #for meta_data in root.iter('meta-data'):
    #  print meta_data.attrib[namespace+'name']
    #
    
    print "\n-------------------------USES-PERMİSSİONS---------------------------------\n"
    
    for uses_permission in root.iter('uses-permission'):
      print uses_permission.attrib[namespace+'name']
    
    
    print "\n---------------------------PERMİSSİONS------------------------------------\n"
    
    for permission in root.iter('permission'):
      print permission.attrib[namespace+'name']
    
    
    print "\n-------------------------USES-FEATURES---------------------------------\n"
 
    if namespace+'name' in root.iter('uses-feature'):
      for uses_feature in root.iter('uses-feature'):
        print uses_feature.attrib[namespace+'name']
    
    
    print "\n++++++++++++++++++++++++++++SERViCES++++++++++++++++++++++++++++++++++++++\n"
    
    for service in root.iter('service'):
      print service.attrib[namespace+'name']
    
    
    print "\n++++++++++++++++++++++++++++RECEIVERS++++++++++++++++++++++++++++++++++++++\n"
    
    for receiver in root.iter('receiver'):
      print receiver.attrib[namespace+'name']
