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
    argparser.add_argument('-output_path', type=str, default=None, help='Write path for the lda model')
    argparser.add_argument('-k', type=int, required=True, help='Number of topics for LDA')
    argparser.add_argument('-passes', type=int, default=200, help='Number of passes for LDA training')
    argparser.add_argument('-lowercase', dest='lowercase', action='store_true')
    argparser.set_defaults(lowercase=True)
    return argparser.parse_args()


def extract_words(documents, pos=None, lowercase=True, use_lemmas=True):
    new_documents = []
    for document in documents:
        new_document = []
        for token in document['Tokens']:
            if token["POS"] == "NOUN":
                if isinstance(pos, list):
                    if not token["POS"] in pos:
                        continue
                if use_lemmas:
                    if token["Lemma"]:
                        value = token["Lemma"][0]
                    else:
                        value = token["Text"]
                else:
                    value = token['Text']
                if lowercase:
                    value = value.lower()
                new_document.append(value)
        if len(new_document) > 0:
            new_documents.append(new_document)
    return new_documents


def call_loading_method(loading_method, documents):
    if loading_method == 'extract_all_words':
        return extract_words(documents, pos=None, lowercase=True, use_lemmas=True)
    elif loading_method == 'extract_nouns':
        return extract_words(documents, pos=['NOUN'], lowercase=True, use_lemmas=True)
    else:
        return None


def load_input_file(input_file, loading_method='extract_all_words', tokenized=True):
    with open(input_file, encoding='utf-8') as data_file:
        data = json.load(data_file)
        if tokenized:
            return call_loading_method(loading_method, data)
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
    corpus = [dictionary.doc2bow(text) for text in documents]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=arguments.k, id2word=dictionary,
                                               passes=arguments.passes)
    logger.info('LDA models trained')
    for i in ldamodel.show_topics(-1, 10):
        print(i)
    if not arguments.output_path:
        logger.info('No output_path specified, no model will be saved to disk')
    else:
        logger.info('Saving LDA models to {}'.format(arguments.output_path))
        ldamodel.save(arguments.output_path)
