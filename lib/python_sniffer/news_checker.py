#!/usr/bin/env python
import os
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.parse.stanford import StanfordParser
from nltk.parse.stanford import StanfordDependencyParser

java_path = "usr/bin/java"
os.environ['JAVAHOME'] = java_path

stanford_parser_dir = '/home/john/Desktop/ruby/smelly-shoes/lib/python_sniffer/stanford_NLP/stanford-parser-full-2015-04-20/'
eng_model_path = stanford_parser_dir + "edu/stanford/nlp/models/lexparser/englishRNN.ser.gz"
my_path_to_models_jar = stanford_parser_dir + "stanford-parser-3.5.2-models.jar"
my_path_to_jar = stanford_parser_dir + "stanford-parser.jar"

parser=StanfordParser(model_path=eng_model_path, path_to_models_jar=my_path_to_models_jar, path_to_jar=my_path_to_jar)
dependency_parser = StanfordDependencyParser(path_to_jar=my_path_to_jar, path_to_models_jar=my_path_to_models_jar)

verb_list = ['said', 'says', 'told', 'described', 'recalls', 'recalled']

def get_voice(relationship):
	for verb in verb_list:
		if verb == relationship[0][0] and relationship[2][1] == 'NNP':
			return relationship[2][0]
		return False

def parse_sentence(sentence, sources):
	print sentence
	#Code below detects relations (passive and active)
	result = dependency_parser.raw_parse(sentence)
	dep = result.next()
	parsed_result = list(dep.triples())
	print parsed_result
	for relationship in parsed_result:
		if relationship[1] == 'nsubj':
			source = get_voice(relationship)
		if source != False and source not in sources:
			sources.append(source)			
	#if one thing, return result
	#If another, return result

def extract_sentences(page_content):
	sources = []
	multiple_source = False
	result = 0
	#ensure this corresponds to the data you're constructing in the parse_sentence function
	sentences_to_parse = sent_tokenize(page_content)
	for sentence in sentences_to_parse:
		result = parse_sentence(sentence, sources)
	print sources
	return result


#extract_sentences('John said the cat was black.') #((u'said', u'VBD'), u'nsubj', (u'John', u'NNP'))
#extract_sentences('The cat was black, John said.') #((u'said', u'VBD'), u'nsubj', (u'John', u'NNP'))
#extract_sentences('Mr Margrave said the issue with reading was it was boring.') #((u'said', u'VBD'), u'nsubj', (u'Margrave', u'NNP'))
#extract_sentences('John is the supervisor and he said.') #((u'said', u'VBD'), u'nsubj', (u'he', u'PRP'))
#extract_sentences('John went to Candy Mountain where he said he got fat.')
#extract_sentences('John is the leader of the local youth group. He said it was fun.')
extract_sentences('John said he loved Mary. She said it was not mutual. Mary said she loved Jim.')

#said, says, told, described, 

