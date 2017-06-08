import itertools
import bz2
from gensim import utils
from gensim.corpora.wikicorpus import extract_pages, IGNORED_NAMESPACES, ARTICLE_MIN_WORDS, remove_markup
from common.gensim_custom import get_all_words
# based on http://radimrehurek.com/topic_modeling_tutorial/2%20-%20Topic%20Modeling.html

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
        tokens = get_all_words(text)
        if len(tokens) < ARTICLE_MIN_WORDS or any(title.startswith(ignore + ':') for ignore in IGNORED_NAMESPACES):
            continue
        yield title, tokens


class WikiCorpusCustom(object):
    def __init__(self, dump_file, dictionary, clip_docs=None):
        """
        Parse the first `clip_docs` Wikipedia documents from file `dump_file`.
        Yield each document in turn, as a list of tokens (unicode strings).

        """
        self.dump_file = dump_file
        self.dictionary = dictionary
        self.clip_docs = clip_docs

    def __iter__(self):
        self.titles = []
        for title, tokens in itertools.islice(iterate_wiki(self.dump_file), self.clip_docs):
            self.titles.append(title)
            yield self.dictionary.doc2bow(tokens)

    def __len__(self):
        return self.clip_docs