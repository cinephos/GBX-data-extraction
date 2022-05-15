# -*- coding: utf-8 -*-
"""
Created on Sun May  8 07:57:02 2022

@author: cinephos
"""
##########################################################################
# This is a simple python code to extract data from gbx files stored     #
# in TM autosaves file. Info retrieved are stored to a text file         #
# The code is tested and works under Spyder 5 software in Windows.       #
##########################################################################
 
import re
import os
import csv
import datetime
import xml.etree.ElementTree as ET
import manialibformat

# path is the Autosaves directory. Use '/' for subfolders even in Windows

path = 'D:/Users/YourUsernameHere/Documents/Trackmania/Replays/Autosaves'
dirs = os.listdir(path)

# The output text file has to be deleted if previously created.

os.remove('txtfile.txt')

# The output text file must include utf-8 characters

txtfile = open('txtfile.txt','w', encoding="utf-8", newline='')
csvwrite = csv.writer(txtfile)

# These are the column headers

fields = ['mod-time', 'NAME-MANIAFORMAT', 'NAME', 'PB','URL', ]
csvwrite.writerow(fields)

# A for loop repeats the instructions for all files in Autosaves dir

for file in dirs:

#   Open the file

    filename = path + '/' + file
    gbxfile = open(filename,'rb') 
    
#   The modification date of the file acyually shows the date when
#   the PB was achieved. It is stored in a simple format. 
      
    modtime = os.path.getmtime(filename)
    modtime = datetime.date.fromtimestamp(modtime).strftime('%Y-%m-%d')
    
#   read the data and find the header. This is done in various steps.
#   The final product is the string xml_header

    gbx_data = gbxfile.read()
    gbx_header = b'(<header)((?s).*)(</header>)'
    header_intermediate = re.findall(gbx_header, gbx_data)
    inter1 = ' '.join([str(item) for item in header_intermediate])
    inter2 = inter1[15:]
    header_middle = inter2[:-16]
    xml_header = '<header' + header_middle + ' </header>'

#   xml_tree is the object containing all header data
#   from its children, the uid, mapname and pb are taken

    xml_tree = ET.fromstring(xml_header)
    for child in xml_tree:
        if child.tag == 'map':
           uid = child.attrib.get('uid')
           name_maniaformat = child.attrib.get('name')
        if child.tag == 'times':
           pb = child.attrib.get('best')

#   The 'remove' function extracts the text from the manialib format

    name = manialibformat.remove(name_maniaformat)
   
#   An extra backslash has to be removed from the name

    name = manialibformat.removebackslash(name)

#   The url to trackmania.io leaderboard page     
    url = 'https://trackmania.io/#/leaderboard/' + uid

#   The txtfile row is created and added to the file
    
    row = [modtime, name_maniaformat, name, pb, url]         
    csvwrite.writerow(row)
    
#   close the input file
   
    gbxfile.close()

# close the output file
    
txtfile.close()    
