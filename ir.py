import sys
import codecs
import json
import gc

with open('./jsonJieba-tran.json', 'r') as f:
  raw_data = json.load(f)

output = {}

for data in raw_data:
  for pos, word in enumerate(data['content'].split()):

    if word not in output:
      output[word] = {}

    if data['id'] not in output[word]:
      output[word][data['id']] = 0

    output[word][data['id']] += 1

del raw_data
gc.collect()

with open('./inverted_index.json', 'w+') as f:
  json.dump(output, f)
