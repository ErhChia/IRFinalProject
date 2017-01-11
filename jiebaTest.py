#incoding=utf-8
import jieba
import json
import sys
import jieba.posseg as pseg

#jieba.set_dictionary("dict.txt.big")
file = open("questions_example.json")
data = json.load(file)

words = pseg.cut("蔡英文")
for word, flag in words:
	word = flag+"/"+word
	print word + " "

#print (", ".join(words))