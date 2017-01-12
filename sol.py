#coding=utf-8
import jieba
import json
from math import log
import os
jieba.load_userdict('NameDict_Ch_v2.txt')
file = open("questions_example.json")
data = json.load(file)
inverted_index = {}
fixed_index = {}
resume_index = []
DOC_NUM = 20
DIR = './split/'
WIKI_NUM = 920017

def create_index(words,question):
	for word in words:
		if word not in inverted_index:
			inverted_index[word] = {}
		if str(question) not in inverted_index[word]:
			inverted_index[word][str(question)] = 0
		inverted_index[word][str(question)] += 1

def tf(query,doc):
	for word,docs in inverted_index.items():
		if query == word:
			return docs[doc]

def idf(query):
	total = 0
	for word,docs in inverted_index.items():
		if query == word:
			for doc in docs.keys():
				total += docs[doc]
	if float(DOC_NUM/total) == 0:
		return 0
	else:
		return log(float(DOC_NUM/total))

def wiki_idf(query):
	fname = DIR + query + '.json'
	if not os.path.isfile(fname):
		return 0 
	data = json.load(open(fname))
	total = len(data)	
	if float(WIKI_NUM/total) ==0:
		return 0
	else:
		return log(float(WIKI_NUM/total))

def tf_idf(query,doc):
	return tf(query,doc)*idf(query)

def findCommon(a_query,q_query):
	q_fname = DIR + q_query + '.json'
	a_fname = DIR + a_query + '.json'
	if not os.path.isfile(q_fname):
		print "q can't open " + q_fname
		return 0
	if not os.path.isfile(a_fname):
		print "a can't open " + a_fname
		return 0
	query = open(q_fname)
	check = open(a_fname)
	count = 0
	q_data = json.load(query)
	a_data = json.load(check)
	for a_doc in a_data.keys():
		for q_doc in q_data.keys():
			if a_doc == q_doc:
				count +=1
	count *= wiki_idf(q_query)
	return count

def return_index(d):
	print len(d)
	for i in range(0,DOC_NUM):
		resume_index.append([])
	for query,docs in d.items():
		for doc in docs.keys():
			#print int(doc)-1
			resume_index[int(doc)-1].append(query)
count = 1
for index in data:
	question = jieba.cut(index['Question'],cut_all=True)
	question = list(question)
	create_index(question,count)
	count += 1
for query,docs in inverted_index.items():
	for doc in docs.keys():
		if(tf_idf(query,doc) >= 2):
			fixed_index[query]=inverted_index[query]

return_index(fixed_index)
answer=[]
count = 1

for index in data:
	commonA = 0
	commonB = 0
	commonC = 0
	a = jieba.cut_for_search(index['A'])
	b = jieba.cut_for_search(index['B'])
	c = jieba.cut_for_search(index['C'])
	print "question" + str(count) + ":"
	print "A=" + index['A']
	print "B=" + index['B']
	print "C=" + index['C']
	for ans in a:
		for query in resume_index[count-1]:
			commonA += findCommon(ans,query)
	for ans in b:
		for query in resume_index[count-1]:
			commonB += findCommon(ans,query)
	for ans in c:
		for query in resume_index[count-1]:
			commonC += findCommon(ans,query)
	print ("commonA = %f"%commonA)
	print ("commonB = %f"%commonB)
	print ("commonC = %f"%commonC)

	if commonA>commonB and commonA>commonC:
		answer.append("A")
	elif commonB>commonA and commonB>commonC:
		answer.append("B")
	elif commonC>commonA and commonC>commonB:
		answer.append("C")
	else:
		answer.append("B")
	count += 1
	print "\n"
print "\n"
print answer
