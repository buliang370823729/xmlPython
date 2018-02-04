# -*- coding: utf-8 -*-
from lxml import etree
import xml.dom.minidom
from xml.dom.minidom import parse,parseString
import wikipedia
import transA
from googleSeaXmlAaa import BSprint,linkListSearch

#create start XML template
plot= etree.Element('top')
doc=etree.ElementTree(plot)
child = etree.SubElement(plot, "resolution")
child.text = "all coflicts resolved"
child1=etree.SubElement(plot,"fallingaction")
child1.text="actions after climax"
child2=etree.SubElement(plot,"climax")
child2.text="all coflicts come to top"
child3 =etree.SubElement(plot,"raisingaction")
child3.text="conflicts are increasing"
child4=etree.SubElement(plot,"exposition")
child4.text="main char introduced"
#assign active xml element
active=child

while True:
	doc=etree.fromstring(etree.tostring(plot))
	outpp=etree.tostring(doc)
	xxml =  xml.dom.minidom.parseString(outpp)
	pret = xxml.toprettyxml()
	print(pret)
#take the second after go command	
	move = raw_input(">").lower().split()
	print(move[1])
	if move[1]=='down':
#goes down the xml if anything it becames active 
		if len(active):
			active=active[0]
		else:
			name= raw_input('>>>>>')
		active=etree.SubElement(active,name.strip())
		textin= raw_input('enter text>>>')
		active.text=transA.multiSer(textin)
# movig back
	elif move[1]=='back':
		var=active.getparent()
		ind=active.getparent().index(active)
		if len(var)==(ind+1):
			name= raw_input('>>>>>')
			active=etree.Element(name)
			var.append(active)
		else:
			active=var[ind+1]
#insert element			
	elif move[1]=='ins':
		inpu= raw_input('>>>>>>')
		par=active.getparent()
		ind=active.getparent().index(active)
		active=etree.Element(inpu.strip())
		par.insert(ind,active)	
#forward		
	elif move[1]=='forw':
		var=active.getparent()
		print (var)
		ind=active.getparent().index(active)
		print(ind)
		if ind==0:
			name= raw_input('>>>>>')
			active=etree.Element(name)
			var.insert(ind,active)
		else:
			active=var[ind-1]
			print(var[ind])
#up			
	elif move[1]=='up':
		active=active.getparent()
		print(etree.tostring(active,pretty_print=True))
#prints active element		
	elif move[1]=="active":
		print(etree.tostring(active))
#writes to file		
	elif move[1]=="write":
		with open('./filename.xml', 'wb') as f: 			f.write(etree.tostring(plot))
#reads from file		
	elif move[1]=="read":
		plot=etree.parse('./filename.xml')
	
	

