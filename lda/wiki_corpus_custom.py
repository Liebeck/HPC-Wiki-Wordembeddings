import itertools
from wiki_iterate import iterate_wiki
# based on http://radimrehurek.com/topic_modeling_tutorial/2%20-%20Topic%20Modeling.html

class WikiCorpusCustom(object):
    def __init__(self, dump_file, dictionary, spacy_ner_grouper, clip_docs=None):
        """
        Parse the first `clip_docs` Wikipedia documents from file `dump_file`.
        Yield each document in turn, as a list of tokens (unicode strings).

        """
        self.dump_file = dump_file
        self.dictionary = dictionary
        self.clip_docs = clip_docs
        self.spacy_ner_grouper = spacy_ner_grouper

    def __iter__(self):
        self.titles = []
        for title, tokens in itertools.islice(iterate_wiki(self.dump_file, self.spacy_ner_grouper), self.clip_docs):
            self.titles.append(title)
            yield self.dictionary.doc2bow(tokens)

    def __len__(self):
        return self.clip_docs