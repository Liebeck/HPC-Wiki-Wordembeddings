# Train word2vec models on Wikipedia
This project contains the PBS job scripts and Python scripts to generate word embeddings from a Wikipedia dump.

The code is from http://textminingonline.com/training-word2vec-model-on-english-wikipedia-by-gensim

We made some modifications for the extraction scripts to keep words longer than 15 characters and to filter out some more MediaWiki stuff. This is especially useful for the German Wikipedia edition.

## How to train the embeddings locally
1. Download https://dumps.wikimedia.org/dewiki/latest/dewiki-latest-pages-articles.xml.bz2
2. python3 wikipedia_extract.py -input_path dewiki-20161120-pages-articles.xml.bz2 -output_path wiki-de_20161120.text
3. python3 wikipedia_train_word2vec.py -input_path wiki-de_20161120.text -output_path word2vec_wiki-de_20161120_400 -dimension 400

## How to train the model on the HILBERT cluster
Please note, there is no dependency management involved and some paths are hardcoded.
1. (Make sure that you downloaded https://github.com/Liebeck/HPC-Logging and placed them into a directory of your choosing.)
2. Download https://dumps.wikimedia.org/dewiki/latest/dewiki-latest-pages-articles.xml.bz2
3. Adjust paths in both job files
4. *qsub -v inputfile=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501-pages-meta-current.xml.bz2,outputfile=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.text wikipedia_extract.job*
5. *qsub -v inputfile=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.text,outputfile=/scratch_gs/malie102/data/wikipedia-de/word2vec_wiki-de_20170501_300,size=300 wikipedia_train_word2vec.job*

## How to train the model on the HILBERT cluster for the German Wikipedia
Please note, there is no dependency management involved and some paths are hardcoded.
1. (Make sure that you downloaded https://github.com/Liebeck/HPC-Logging and placed them into a directory of your choosing.)
2. Download https://dumps.wikimedia.org/dewiki/latest/dewiki-latest-pages-articles.xml.bz2
3. Adjust paths in both job files
4. *qsub -v inputfile=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501-pages-meta-current.xml.bz2,outputfile=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text wikipedia_extract.job*
5. *qsub -v inputfile=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,outputfile=/scratch_gs/malie102/data/wikipedia-de/word2vec_wiki-de_20170501_300,size=300 wikipedia_train_word2vec.job*

## Dependencies
* gensim
* gfortran
