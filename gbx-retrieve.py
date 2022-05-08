# -*- coding: utf-8 -*-
"""
Created on Sun May  8 07:57:02 2022

@author: cinephos
"""
##########################################################################
# This is a simple python code to extract data from gbx files stored     #
# in TM autosaves file. Info retrieved are map uid code, map name and pb.#
# The code is tested and works under Spyder 5 software in Windows.       #
##########################################################################
 
import re
import os
import xml.etree.ElementTree as ET

#path is the Autosaves directory. Use '/' for subfolders even in Windows

path = 'D:/Users/YourUsernameHere/Documents/Trackmania/Replays/Autosaves'
dirs = os.listdir(path)

# A for loop repeats the instructions for all files in Autosaves dir

for file in dirs:

#   Open the file

    filename = path + '/' + file
    gbxfile = open(filename,'rb')    

#   read the data and find the header. This is done in various steps.
#   The final product is the string 'headerout' with the xml header

    data = gbxfile.read()
    stri = data.find(b'\xff\xc0')
    header = b'(<header)((?s).*)(</header>)'
    out = re.findall(header, data)
    out1 = ' '.join([str(item) for item in out])
    out12 = out1[15:]
    outmid = out12[:-16]
    headerout = '<header' + outmid + ' </header>'

#   route is the object containing all header data
#   from its children, the uid, mapname and pb are taken

    route = ET.fromstring(headerout)
    for child in route:
        if child.tag == 'map':
           uid = child.attrib.get('uid')
           name = child.attrib.get('name')
        if child.tag == 'times':
           pb = child.attrib.get('best')

#   the output is printed on the console
             
    print(uid, name, pb)
    
#   close the file
   
    gbxfile.close()
