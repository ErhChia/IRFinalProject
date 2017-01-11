#coding:utf-8
import ijson
import sys
import codecs
import json

def create_index(infile,outfile):
	inverted_index = []
	data = ijson.items(infile,"item")
	docNum = 1
	for index in data:
		for word in index['content'].split():
			if not inverted_index:
				inverted_index.append({"query":word,"document":{index['title']:1}})
			else:
				if  not any(inner_index['query'] == word for inner_index in inverted_index):
					print "word not in inverted index, append"
					inverted_index.append({"query":word,"document":{index['title']:1}})
				else:					
					print "word in inverted index"
					if inverted_index[inverted_index.index((inner_index for inner_index in inverted_index if inner_index['query'] == word).next())]['document'].get(index['title'],False):
						print "title already in inverted index, add value"
						inverted_index[inverted_index.index((inner_index for inner_index in inverted_index if inner_index['query'] == word).next())]['document'][index['title']] += 1
					else:
						print "title not in inverted index, update"
						inverted_index[inverted_index.index((inner_index for inner_index in inverted_index if inner_index['query'] == word).next())]['document'][index['title']] = 1			
		print "\n"
	output = json.dumps(inverted_index, indent=4, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode('utf-8')
	outfile.write(output)
   	#content = ijson.items(fin, 'content')
   	#title = ijson.items(fin, 'title'


    #'''for k, v in tokens.items():
     #   for word in v.lower().split():
      #      if inverted_index.get(word,False):
       #         if k not in inverted_index[word]:
        #            inverted_index[word].append(k)
         #   else:
          #      inverted_index[word] = [k]
    #return inverted_index'''
with open(sys.argv[1],"r") as infile, open('inverted_index.json',"w") as outfile:
	create_index(infile,outfile)