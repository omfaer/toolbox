#!/usr/bin/python
# -*- coding: utf-8 -*-
# version:0.4.0 (Hata yakalama eklendi. Her 100 argümanda bir bekle.)

import xml.etree.ElementTree as ET
import sys
import getopt
import sqlite3 as sqlite
import time 

args_number=0
with sqlite.connect('/dpart/db/SDataS.db') as db:
  cursor=db.cursor()
#with open("/home/omfaer/desktop/info_apk.txt","a") as dosya:
  for xml_file in sys.argv:
   args_number += 1
   if args_number % 100 == 0:
       time.sleep(5)
   if xml_file!=sys.argv[0]:
    try:
      manifest = ET.parse(xml_file)
      root = manifest.getroot()
      namespace = '{http://schemas.android.com/apk/res/android}'
      # note = "Güncellenmiş Uygulamaları takip edebilmek adına version bilgisi vs tutmak hatta buna göre sorgulamak gerekebilir."
      #print "root tag: ", root.tag
      #print "root attrib: ", root.attrib
      print ("\033[0;37;44m " + xml_file + "\033[0;0;0m")
      # cursor.execute("""UPDATE ApkInfo SET versionName=?, versionCode=? WHERE packageName=?""",(root.attrib['platformBuildVersionName'], root.attrib['platformBuildVersionCode'], root.attrib['package']))
      
      print "\n-------------------------PACKAGE-INFORMATİONS---------------------------------\n"
      
      if 'package' in root.attrib:
        print "package-name: ", root.attrib['package']
        cursor.execute("""SELECT packageName FROM AppInfo WHERE packageName=?""",[root.attrib['package']])
        data = cursor.fetchone()
        if data is not None:
          # dosya.write("package-name: " + root.attrib['package'] + "\n" )     
          if 'platformBuildVersionName' in root.attrib:
            print "version-name: ", root.attrib['platformBuildVersionName']
          # dosya.write("version-name: " +  root.attrib['platformBuildVersionName'] + "\n")
            cursor.execute("""UPDATE AppInfo SET versionName=? WHERE packageName=?""",(root.attrib['platformBuildVersionName'], root.attrib['package']))
          else:
            print "Version Name bulunamadı"
          
          if 'platformBuildVersionCode' in root.attrib:
            print "version-code: ", root.attrib['platformBuildVersionCode']
            cursor.execute("""UPDATE AppInfo SET versionCode=? WHERE packageName=?""",(root.attrib['platformBuildVersionCode'], root.attrib['package']))
          else:
            print "Version Code bulunamadı"
          
          print "\n----------USES-PERMİSSİONS-------------\n"

          for uses_permission in root.iter('uses-permission'):
            print uses_permission.attrib[namespace+'name']
            cursor.execute("""INSERT INTO Permissions(permissionName, appInfoId) VALUES(?,(SELECT appInfoId FROM AppInfo WHERE packageName=?))""",(uses_permission.attrib[namespace+'name'], root.attrib['package']))

          print "\n************PERMİSSİONS**************\n"
          
          for permission in root.iter('permission'):
            print permission.attrib[namespace+'name']
          

#          print "\n+++++++++++USES-FEATURES+++++++++++++\n"
#
#          for uses_feature in root.iter('uses-feature'):
#            print uses_feature.attrib[namespace+'name']
#            cursor.execute("""INSERT INTO Features(featureName, appInfoId) VALUES(?,(SELECT appInfoId FROM AppInfo WHERE packageName=?))""",(uses_feature.attrib[namespace+'name'], root.attrib['package']))
#
          print "\n------------SERViCES-----------\n"

          for service in root.iter('service'):
            print service.attrib[namespace+'name'] 
            cursor.execute("""INSERT INTO Services(serviceName, appInfoId) VALUES(?,(SELECT appInfoId FROM AppInfo WHERE packageName=?))""",(service.attrib[namespace+'name'], root.attrib['package']))

          print "\n***********RECEIVERS**********\n"

          for receiver in root.iter('receiver'):
            print receiver.attrib[namespace+'name']
            cursor.execute("""INSERT INTO Receivers(receiverName, appInfoId) VALUES(?,(SELECT appInfoId FROM AppInfo WHERE packageName=?))""",(receiver.attrib[namespace+'name'], root.attrib['package']))
          
          db.commit()
        else:
          print "Paket ismi veritabanında yok: ",root.attrib['package']
    except Exception as e:
      print ("\033[0;37;44m " + xml_file + "dosyasında hata \033[0;0;0m")
      with open("/home/omfaer/sarge/insert_db_errors.txt","a") as err:
        err.write("Hata veren dosya:" + xml_file +"\n")
        err.write("Verdiği hata:" + str(e) +"\n\n\n\n")
