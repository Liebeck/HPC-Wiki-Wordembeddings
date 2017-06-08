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
    argparser.add_argument('-output_path', type=str, required=True, help='Write path for the lda model')
    # argparser.add_argument('-k', type=str, required=True, help='Number of topics for LDA')
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

    # logger.info("k: " + str(arguments.k))
    #iterate_wiki(arguments.input_path)
    #for title, tokens in iterate_wiki(arguments.input_path):
    # print(title)
    #for title, tokens in itertools.islice(iterate_wiki(arguments.input_path), 8):
        #print(title, tokens[:10])  # print the article title and its first ten tokens
    #space_ner_grouper = SpacyNERGrouper()

    # Create the dictionary
    doc_stream = (tokens for _, tokens in iterate_wiki(arguments.input_path))
    wiki_id2word_dictionary = gensim.corpora.Dictionary(doc_stream)
    print(wiki_id2word_dictionary)
    wiki_id2word_dictionary.filter_extremes(no_below=20, no_above=0.1)
    print(wiki_id2word_dictionary)
    wiki_id2word_dictionary.dictionary.save_as_text(arguments.output_path + '_wordids.txt.bz2')

    # create bag of words representation
    wiki_corpus = WikiCorpusCustom(arguments.input_path, wiki_id2word_dictionary)
    gensim.corpora.MmCorpus.serialize(arguments.output_path + '_bow.mm', wiki_corpus)

    # serialize tfidf
    mm = MmCorpus(arguments.output_path + '_bow.mm')
    tfidf = TfidfModel(mm, id2word=wiki_id2word_dictionary, normalize=True)
    tfidf.save(arguments.output_path + '.tfidf_model')
    MmCorpus.serialize(arguments.output_path + '_tfidf.mm', tfidf[mm], progress_cnt=10000)
