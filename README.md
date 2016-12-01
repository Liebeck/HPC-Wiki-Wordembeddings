# HPC-Wiki-Wordembeddings
This project contains the PBS job scripts and Python scripts to generate word embeddings from a Wikipedia dump.
Please note, there is no dependency management involved and some paths are hardcoded.

## How to train the model on the HILBERT cluster
The code is from http://textminingonline.com/training-word2vec-model-on-english-wikipedia-by-gensim


1. (Make sure that you downloaded https://github.com/Liebeck/HPC-Logging and placed them into a directory of your choosing.)
2. Clone the repository
3. Download https://dumps.wikimedia.org/dewiki/latest/dewiki-latest-pages-articles.xml.bz2
4. Adjust paths in both job files
5. *qsub de-wiki-extract.job*
6. *qsub de-wiki_wordembeddings.job*

## How to train the embeddings locally
1. Download the latest dump
2. python process_wiki.py dewiki-20161120-pages-articles.xml.bz2 wiki-de_20161120.text
