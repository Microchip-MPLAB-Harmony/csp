import xml.etree.ElementTree as ET
import os
path = "./"
files = os.listdir(path)
for name in files:
	if ".xml" in name:
		tree = ET.parse('./' + str (name))
		root = tree.getroot()
		root.set('id', name.split(".xml")[0])
		tree.write('./' + str (name))
	
		fo_xml = open("./" + str(name), "r+")
		content = fo_xml.read()
		fo_xml.seek(0, 0)
		fo_xml.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>" + '\n' + content)
		fo_xml.close()