#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Code from tutorial: http://textminingonline.com/training-word2vec-model-on-english-wikipedia-by-gensim
import logging
import os.path
import sys
import argparse
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


def config_argparser():
    argparser = argparse.ArgumentParser(description='Wikipedia train word2vec')
    argparser.add_argument('-input_path', type=str, required=True, help='Path to the preprocessed Wikipedia dump')
    argparser.add_argument('-output_path', type=str, required=True, help='Write path for the word2vec models')
    argparser.add_argument('-dimension', type=int, help='Size of the embeddings')
    return argparser.parse_args()


if __name__ == '__main__':
    arguments = config_argparser()
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
    logger.info("Input path wiki: " + arguments.input_path)
    logger.info("Word embedding output path: " + arguments.output_path)
    logger.info("Size: " + str(arguments.dimension))
    model = Word2Vec(LineSentence(arguments.input_path), size=arguments.dimension, window=5, min_count=5, workers=20)
    # trim unneeded model memory = use (much) less RAM
    model.init_sims(replace=True)
    model.save(arguments.output_path + "_binary")
    model.save_word2vec_format(arguments.output_path, binary=False)
