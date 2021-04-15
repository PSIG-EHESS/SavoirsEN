#!/usr/bin/env python
# coding: utf8

import xml.etree.ElementTree as ET

tree = ET.parse("BNU_01_Didier.xml")

for n in tree.iter('placeName'):  
	print(n)    
		
