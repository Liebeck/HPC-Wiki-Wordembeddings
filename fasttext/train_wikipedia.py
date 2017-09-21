from gensim.models.wrappers.fasttext import FastText as FT_wrapper


def train_wikipedia(ft_home, input_path, output_path, iterations=5, min_n=3, max_n=3):
    model = FT_wrapper.train(ft_home, input_path, min_n=min_n, max_n=max_n, iter=iterations)
    model.save(output_path)


if __name__ == '__main__':
    ft_home = '/home/admin2/ExternCode/fastText/fasttext'
    input_path = 'dewiki-20170501.custom.text'
    iterations = [5, 20, 100, 200, 300]
    ngram_ranges = [(3, 3), (4, 4), (5, 5), (6, 6), (3, 6)]
    for iteration in iterations:
        for ngram_range in ngram_ranges:
            output_path = 'dewiki-20170501-{}_{}-{}'.format(ngram_range[0], ngram_range[1], iteration)
            print(output_path)
            train_wikipedia(ft_home, input_path, output_path, iteration, ngram_range[0], ngram_range[1])
