#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Code from tutorial: http://textminingonline.com/training-word2vec-model-on-english-wikipedia-by-gensim

import logging
import os.path
import sys
import six
import argparse
from gensim.corpora import WikiCorpus


def config_argparser():
    argparser = argparse.ArgumentParser(description='Wikipedia Dump Extractor')
    argparser.add_argument('-input_path', type=str, required=True, help='Path to the raw Wikipedia dump')
    argparser.add_argument('-output_path', type=str, required=True, help='Write path for extracted text content')
    return argparser.parse_args()


if __name__ == '__main__':
    arguments = config_argparser()
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
    logger.info("Input corpus path: " + arguments.input_path)
    logger.info("Output path: " + arguments.output_path)
    space = u' '
    i = 0
    output = open(arguments.output_path, 'w')
    wiki = WikiCorpus(arguments.input_path, lemmatize=False, dictionary={})
    for text in wiki.get_texts():
        # article = space.join([t.decode("utf-8") for t in text])
        # output.write("{}\n".format(article.encode("utf-8")))
        if six.PY3:
            article = space.join([t.decode("utf-8") for t in text])
        else:
            article = space.join(text) + "\n"
        output.write("{}\n".format(article))
        i = i + 1
        if (i % 10000 == 0):
            logger.info("Saved " + str(i) + " articles")

    output.close()
    logger.info("Finished Saved " + str(i) + " articles")
