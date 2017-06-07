#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import argparse
import os
import sys
import json
import gensim
from gensim import corpora, models


def config_argparser():
    argparser = argparse.ArgumentParser(description='Wikipedia train word2vec')
    argparser.add_argument('-input_file', type=str, required=True, help='Path to the raw Wikipedia dump')
    argparser.add_argument('-tokenized', dest='tokenized', action='store_true')
    argparser.set_defaults(tokenized=True)
    argparser.add_argument('-loading_method', type=str, default='extract_all_words')
    # argparser.add_argument('-output_path', type=str, required=True, help='Write path for the lda model')
    argparser.add_argument('-k', type=str, required=True, help='Number of topics for LDA')
    return argparser.parse_args()


def extract_all_words(documents):
    new_documents = []
    for document in documents:
        new_document = []
        for token in document['Tokens']:
            new_document.append(token['Text'])
        new_documents.append(new_document)
    return new_documents


def get_loading_method(loading_method):
    if loading_method == 'extract_all_words':
        return extract_all_words
    else:
        return None


def load_input_file(input_file, loading_method='extract_all_words', tokenized=True):
    with open(input_file, encoding='utf-8') as data_file:
        data = json.load(data_file)
        if tokenized:
            loading_method = get_loading_method(loading_method)
            return loading_method(data)
        else:
            return None


if __name__ == '__main__':
    arguments = config_argparser()
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
    documents = load_input_file(arguments.input_file, loading_method=arguments.loading_method,
                                tokenized=arguments.tokenized)
    dictionary = corpora.Dictionary(documents)
    print(str(len(dictionary)))
    corpus = [dictionary.doc2bow(text) for text in documents]
    passes = 50
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=arguments.k, id2word=dictionary, passes=passes)
    ldamodel.print_topics()
    # todo: train LDA
    # todo: save results in file system
