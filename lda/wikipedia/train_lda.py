import argparse
import bz2
import gensim


def config_argparser():
    argparser = argparse.ArgumentParser(description='WikipediaLDA')
    argparser.add_argument('-basepath', type=str, required=True,
                           help='Path to the directory containing the Wikipedia files')
    argparser.add_argument('-k', type=str, required=True, help='Number of topics for LDA')
    return argparser.parse_args()


if __name__ == '__main__':
    arguments = config_argparser()
    id2word = gensim.corpora.Dictionary.load_from_text(bz2.BZ2File(arguments.basepath + '_wordids.txt.bz2'))
    mm = gensim.corpora.MmCorpus(arguments.basepath + '_tfidf.mm')
    lda = gensim.models.ldamodel.LdaModel(corpus=mm, id2word=id2word, num_topics=arguments.k, update_every=1,
                                          chunksize=10000, passes=1)
    lda.save(arguments.basepath + 'lda_{}.lda'.format(arguments.k))
