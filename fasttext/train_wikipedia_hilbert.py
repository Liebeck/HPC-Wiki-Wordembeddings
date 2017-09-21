from gensim.models.wrappers.fasttext import FastText as FT_wrapper

import argparse


def config_argparser():
    argparser = argparse.ArgumentParser(description='fastText train on HILBERT')
    argparser.add_argument('-input_file', type=str, required=True, help='Path to the Wikipedia text')
    argparser.add_argument('-fasttext_path', type=str, required=True, help='Path to fastText')
    argparser.add_argument('-output_path', type=str, default=None, help='Write path for the fastText model')
    argparser.add_argument('-iterations', type=int, required=True, help='Number of training iterations')
    argparser.add_argument('-min_n', type=int, required=True, help='Min length of char ngram')
    argparser.add_argument('-max_n', type=int, required=True, help='Max length of char ngram')
    return argparser.parse_args()


def train_wikipedia(ft_home, input_path, output_path, iterations=5, min_n=3, max_n=3):
    model = FT_wrapper.train(ft_home, input_path, min_n=min_n, max_n=max_n, iter=iterations)
    model.save(output_path)


if __name__ == '__main__':
    arguments = config_argparser()
    train_wikipedia(arguments.fasttext_path, arguments.input_file, arguments.output_path, arguments.iterations,
                    arguments.min_n, arguments.max_n)
