from gensim import utils


def tokenize_new(content):
    return [token for token in utils.tokenize(content, lower=True, errors='ignore')
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
