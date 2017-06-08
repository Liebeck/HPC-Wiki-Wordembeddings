#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os.path
import sys
import argparse
import gensim
from lda.wikipedia.wiki_corpus_custom import WikiCorpusCustom
from gensim.corpora import MmCorpus
from gensim.models import TfidfModel
from lda.wikipedia.wiki_corpus_custom import iterate_wiki
import itertools


def config_argparser():
    argparser = argparse.ArgumentParser(description='Wikipedia train word2vec')
    argparser.add_argument('-input_path', type=str, required=True, help='Path to the raw Wikipedia dump')
    argparser.add_argument('-output_path', type=str, required=True, help='Write path for the processed dump')
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
    doc_stream = (tokens for _, tokens in itertools.islice(iterate_wiki(arguments.input_path), 1000))
    wiki_id2word_dictionary = gensim.corpora.Dictionary(doc_stream)
    wiki_id2word_dictionary.filter_extremes(no_below=20, no_above=0.1)
    wiki_id2word_dictionary.save_as_text(arguments.output_path + '_wordids.txt.bz2')
    wiki_corpus = WikiCorpusCustom(arguments.input_path, wiki_id2word_dictionary)
    gensim.corpora.MmCorpus.serialize(arguments.output_path + '_bow.mm', wiki_corpus)
    mm = MmCorpus(arguments.output_path + '_bow.mm')
    tfidf = TfidfModel(mm, id2word=wiki_id2word_dictionary, normalize=True)
    tfidf.save(arguments.output_path + '.tfidf_model')
    MmCorpus.serialize(arguments.output_path + '_tfidf.mm', tfidf[mm], progress_cnt=10000)
