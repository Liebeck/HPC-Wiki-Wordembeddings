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