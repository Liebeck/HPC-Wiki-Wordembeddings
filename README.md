# HPC-Wiki-Wordembeddings
This project contains the PBS job scripts and Python scripts to generate word embeddings from a Wikipedia dump.
Please note, there is no dependency management involved and some paths are hardcoded.

# How to train the model
The code is from http://textminingonline.com/training-word2vec-model-on-english-wikipedia-by-gensim
2. Clone the repository
3. Download https://dumps.wikimedia.org/dewiki/latest/dewiki-latest-pages-articles.xml.bz2
4. Adjust paths in both job files
5. *qsub de-wiki-extract.job*
6. *qsub de-wiki_wordembeddings.job*