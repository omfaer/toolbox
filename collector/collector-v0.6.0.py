#!/usr/bin/python
# -*- coding: utf-8 -*-
# version:0.6.0 (Kötücül Apkların Manifest dosyaları ve kategorilendirme için.)

import xml.etree.ElementTree as ET
import sys
import getopt
import sqlite3 as sqlite
import time
import sha3

args_number=0
with sqlite.connect('/home/omfaer/prison-test-db.db') as db:
  cursor=db.cursor()
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

      if 'package' in root.attrib:
      	package_name = root.attrib['package']
        print "package-name: ", package_name

        print "\n----------USES-PERMISSIONS-------------\n"
        joinstr = package_name
        
        for uses_permission in root.iter('uses-permission'):
          print uses_permission.attrib[namespace+'name']
          joinstr = joinstr + "||" + uses_permission.attrib[namespace+'name'] 

        print "\n************PERMISSIONS**************\n"
          
        for permission in root.iter('permission'):
          print permission.attrib[namespace+'name']
	  joinstr = joinstr + "||" + permission.attrib[namespace+'name']

	hash_str = sha3.sha3_224(joinstr.encode('utf-8')).hexdigest()


        cursor.execute("""SELECT pbHash FROM AppInfo WHERE pbHash=?""",[hash_str])
        data = cursor.fetchone()
        if data is None:
          cursor.execute("""INSERT INTO AppInfo(packageName, pbHash) VALUES(?,?) """, (root.attrib['package'], hash_str))
  
          print "\n******************************CATEGORY-CLASS**********************************\n"
          cursor.execute("""INSERT INTO Categories(categoryName, appInfoId) VALUES(?,(SELECT appInfoId FROM AppInfo WHERE pbHash=?))""",(category, hash_str))
  
          cursor.execute("""INSERT INTO Classification(classificationName, appInfoId) VALUES(?,(SELECT appInfoId FROM AppInfo WHERE pbHash=?))""",("malware",hash_str))
        
  
          print "\n-------------------------PACKAGE-INFORMATIONS---------------------------------\n"
        
          print "package-name: ", root.attrib['package']
          cursor.execute("""SELECT packageName FROM AppInfo WHERE pbHash=?""",[hash_str])
          data = cursor.fetchone()
          if data is not None:
            if 'platformBuildVersionName' in root.attrib:
              print "version-name: ", root.attrib['platformBuildVersionName']
              cursor.execute("""UPDATE AppInfo SET versionName=? WHERE pbHash=?""",(root.attrib['platformBuildVersionName'], hash_str))
            else:
              print "Version Name bulunamadı"
             
            if 'platformBuildVersionCode' in root.attrib:
              print "version-code: ", root.attrib['platformBuildVersionCode']
              cursor.execute("""UPDATE AppInfo SET versionCode=? WHERE pbHash=?""",(root.attrib['platformBuildVersionCode'], hash_str))
            else:
              print "Version Code bulunamadı"
            
            print "\n----------USES-PERMISSIONS-------------\n"
  
            for uses_permission in root.iter('uses-permission'):
              print uses_permission.attrib[namespace+'name']
              cursor.execute("""INSERT INTO Permissions(permissionName, appInfoId) VALUES(?,(SELECT appInfoId FROM AppInfo WHERE pbHash=?))""",(uses_permission.attrib[namespace+'name'], hash_str))
  
            print "\n************PERMISSIONS**************\n"
            
            for permission in root.iter('permission'):
              print permission.attrib[namespace+'name']
            
            print "\n------------SERVICES-----------\n"
  
            for service in root.iter('service'):
              print service.attrib[namespace+'name'] 
              cursor.execute("""INSERT INTO Services(serviceName, appInfoId) VALUES(?,(SELECT appInfoId FROM AppInfo WHERE pbHash=?))""",(service.attrib[namespace+'name'], hash_str))
  
            print "\n***********RECEIVERS**********\n"
  
            for receiver in root.iter('receiver'):
              print receiver.attrib[namespace+'name']
              cursor.execute("""INSERT INTO Receivers(receiverName, appInfoId) VALUES(?,(SELECT appInfoId FROM AppInfo WHERE pbHash=?))""",(receiver.attrib[namespace+'name'], hash_str))
            
            db.commit()
          else:
            print "Paket ismi veritabanında yok: ",root.attrib['package']
        else:
          print "Veritabanında zaten var"
    except Exception as e:
      print ("\033[0;37;44m " + xml_file + "dosyasında hata \033[0;0;0m")
      print ("\nVerdiği Hata: " + str(e) + "\n")
      with open("/home/omfaer/errors-new-collector.txt","a") as err:
        err.write("Hata veren dosya:" + xml_file +"\n")
        err.write("Verdiği hata:" + str(e) +"\n\n\n\n")
