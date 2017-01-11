# coding=utf-8
import ijson
import json
import os
DATA_DIR = 'inverted_index'

if not os.path.isdir(DATA_DIR):
	os.mkdir(DATA_DIR)

def saveDictToFile(data, f_name):
	f_name = "{0}/{1}.json".format(
			DATA_DIR,
			f_name.replace('/','_')
		)
	with open (f_name,'w+') as f:
		json.dump(data,f)

with open('./inverted_index.json', 'r') as f:
	now_word = ""
	data = {}
	counter = 0
	for prefix, event, value in ijson.parse(f):
		if event is not "number":
			continue
with open('./inverted_index.json', 'r') as f:
	now_word = ""
	data = {}
	for prefix, event, value in ijson.parse(f):
		if event is not "number":
			continue
		
		word, p_id = prefix.split('.')

		if word != now_word:
			saveDictToFile(data, word)
			splited_data = {}
			now_word = word

		data[p_id] = value
		print (word, splited_data)
# 讀完最後一次存檔
saveDictToFile(data, word)