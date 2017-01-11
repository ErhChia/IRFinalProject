import ijson
import json
import os 
DATA_DIR = 'inverted_index'

if not os.path.isdir(DATA_DIR):
	os.mkdir(DATA_DIR)

def saveDictToFile(data, f_name):
	f_name = "{0}/{1}".format(
			DATA_DIR,
			f_name.replace('/','_')
		)
	with open(f_name,'w+') as f:
		json.dumps(data,f,ensure_ascii=False).encode('utf-8')

with open('inverted_index.json') as f:
	now_word = ""
	data = {}
	counter = 0
	for prefix, event, value in ijson.parse(f):
		if event is not "number":
			continue
		word,p_id = prefix.split('.')

		if word != now_word:
			counter += 1
			saveDictToFile(data,word)
			split_data = {}
			now_word = word

		data[p_id] = value

		if counter >10:
			break

saveDictToFile(data,word)