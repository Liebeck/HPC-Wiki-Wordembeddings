#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import bz2
import logging
import os.path
import sys
from gensim import utils
from gensim.corpora.wikicorpus import extract_pages, IGNORED_NAMESPACES, ARTICLE_MIN_WORDS, remove_markup


def config_argparser():
    argparser = argparse.ArgumentParser(description='Wikipedia Dump Extractor')
    argparser.add_argument('-input_path', type=str, required=True, help='Path to the raw Wikipedia dump')
    argparser.add_argument('-output_path', type=str, required=True, help='Write path for extracted text content')
    return argparser.parse_args()


def tokenize_new(content):
    return [token.encode('utf8') for token in utils.tokenize(content, lower=True, errors='ignore')
            if 2 <= len(token) and not token.startswith('_')]


def get_all_words(text):
    text = filter_file_links(text)
    return tokenize_new(text.replace('[', '').replace(']', ''))


def filter_file_links(text):
    '''
     In order to remove '[[File: ]]' entries, we decided to split the article's text into multiple lines and to
     remove every line that contains '[[File::'. We tried other approaches but some outlier still remained.
     Therefore, we are greedy in removing lines.
    '''
    lines = text.split('\n')
    lines = [x for x in lines if not ('[[File:' in x)]
    text = '\n'.join(lines)
    return text


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
    lemmatize = utils.has_pattern()
    filter_namespaces = ('0',)
    texts = ((text, lemmatize, title, pageid) for title, text, pageid in
             extract_pages(bz2.BZ2File(arguments.file_path), filter_namespaces))
    parsed_articles = []
    parsed_article_counter = 0
    space = u' '
    output = open(arguments.output_path, 'w')
    for article in texts:
        text, lemmatize, title, pageid = article
        text = utils.to_unicode(text, 'utf8', errors='ignore')
        text = utils.decode_htmlentities(text)  # '&amp;nbsp;' --> '\xa0'
        text = remove_markup(text)
        tokens = get_all_words(text)
        if len(tokens) < ARTICLE_MIN_WORDS or any(title.startswith(ignore + ':') for ignore in IGNORED_NAMESPACES):
            continue
        output.write("{}\n".format(space.join(tokens) + "\n"))
        parsed_article_counter += 1
    print('Parsed articles: {}', parsed_article_counter)
