#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Code from tutorial: http://textminingonline.com/training-word2vec-model-on-english-wikipedia-by-gensim

import logging
import os.path
import sys

from gensim.corpora import WikiCorpus

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
    # check and process input arguments
    if len(sys.argv) < 3:
        sys.exit(1)
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    logger.info("Input corpus path: " + input_path)
    logger.info("Output path: " + output_path)
    space = u' '
    i = 0
    output = open(output_path, 'w')
    wiki = WikiCorpus(input_path, lemmatize=False, dictionary={})
    for text in wiki.get_texts():
        article = space.join([t.decode("utf-8") for t in text])
        output.write("{}\n".format(article.encode("utf-8")))
        i = i + 1
        if (i % 10000 == 0):
            logger.info("Saved " + str(i) + " articles")

    output.close()
    logger.info("Finished Saved " + str(i) + " articles")
