import bz2
from gensim import utils
from gensim.corpora.wikicorpus import extract_pages, IGNORED_NAMESPACES, ARTICLE_MIN_WORDS, remove_markup
from common.gensim_custom import get_all_words_grouped


def iterate_wiki(input_path, spacy_ner_grouper):
    lemmatize = utils.has_pattern()
    filter_namespaces = ('0',)
    texts = ((text, lemmatize, title, pageid) for title, text, pageid in
             extract_pages(bz2.BZ2File(input_path), filter_namespaces))
    for article in texts:
        text, lemmatize, title, pageid = article
        text = utils.to_unicode(text, 'utf8', errors='ignore')
        text = utils.decode_htmlentities(text)  # '&amp;nbsp;' --> '\xa0'
        text = remove_markup(text)
        tokens = get_all_words_grouped(text, spacy_ner_grouper)
        if len(tokens) < ARTICLE_MIN_WORDS or any(title.startswith(ignore + ':') for ignore in IGNORED_NAMESPACES):
            continue
        yield title, tokens
