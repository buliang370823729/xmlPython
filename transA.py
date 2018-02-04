# This Python file uses the following encoding: utf-8
# -*- coding: utf-8 -*-
import translate
import wikipedia
import sys
reload(sys)
import locale
sys.setdefaultencoding(locale.getpreferredencoding())
from translate import Translator
#translates given word from lang
def Trans(slovo,from_l,to_l):
	translator=Translator(from_lang=from_l,to_lang=to_l)
	rtr="output"
	try:
		rtr=translator.translate(slovo)
	finally:
		return rtr
#search wikipedia,gives summ of second result
def wiki(serch,lang):
	res=["no page"]
	resde=[]
	resultat=["."]
	wikipedia.set_lang(lang)
	try:
		res=wikipedia.search(serch)
		print(res)
		for deco in res:
			theline=repr(deco).decode("unicode_escape").encode("utf-8")
			print(theline)
			resde.append(theline)
			print (	','.join(resde))

	except wikipedia.exceptions.PageError as e:
		print("no such page" + e)
	debugres=resde
	###debugres = debugres.decode('utf-8')
	print("res>>>>"+str(debugres))
	if len(resde)!=0:
		try:
			resultat=wikipedia.summary(	','.join(resde[1])-"u", sentences=3)
			print(">>>>>>>!!!!!"+''.join(resde[1]-"u"))
		except wikipedia.exceptions.DisambiguationError as e:
			print (e.options[0])
	else:
		resultat=["."]

	return resultat
#takes word on ru  search wiki,transl on en, then adds en search, transl on ru
def multiSer(fromXml):
	pervChast=wiki(fromXml,"ru")
	perev=Trans(fromXml,"ru","en")
	tr=wiki(perev,"en")
	vtorChast=Trans(tr,"en","ru")
	result=(pervChast+vtorChast)
	return result
	
	
