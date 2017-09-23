# Train fastText character n-gram embeddings

We use Gensim to train character n-gram embeddings on Wikipedia. As of today (2017-09-21), Gensim does only provide a wrapper Facebook's fastText and the native Python implementation is still in the development branch and not stable.

## Train the models locally
1. pip install Cython
2. Build fastText
``` bash
git clone https://github.com/facebookresearch/fastText.git
cd fastText
make
```
3. pip install Gensim
4. Use word2vec/wikipedia_extract_custom.py to extract raw text from a Wikipedia dump
5. Open train_wikipedia and adjust the path to the locally installed fastText and the input path to the extracted text from the dump
6. python train_wikipedia.py


## HILBERT scripts
``` bash
qsub -v inputfile=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,output_path=/scratch_gs/malie102/data/fasttext/dewiki-20170501-3_3-5,fasttext_path=/scratch_gs/malie102/code/fastText/fasttext,iterations=5,min_n=3,max_n=3 train_wikipedia_hilbert.job
```



