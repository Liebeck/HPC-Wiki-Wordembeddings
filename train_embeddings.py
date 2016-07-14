#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Code from tutorial: http://textminingonline.com/training-word2vec-model-on-english-wikipedia-by-gensim
import logging
import os.path
import sys
import multiprocessing
 
from gensim.corpora import  WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
 
 
if __name__ == '__main__':
	program = os.path.basename(sys.argv[0])
	logger = logging.getLogger(program)
	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
	logging.root.setLevel(level=logging.INFO)
	logger.info("running %s" % ' '.join(sys.argv))
	# check and process input arguments
	input_path_wiki = sys.argv[1]
	output_embedding_path = sys.argv[2]
	logger.info("Input path wiki: " + input_path_wiki)
	logger.info("Word embedding output path: " + output_embedding_path)
	if len(sys.argv) < 3:
		sys.exit(1)

	model = Word2Vec(LineSentence(input_path_wiki), size=400, window=5, min_count=5, workers=20)
	# trim unneeded model memory = use (much) less RAM
	model.init_sims(replace=True)

	model.save(output_embedding_path)
	model.save_word2vec_format(output_embedding_path + "_non_binary", binary=False)