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
qsub -v input_file=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,output_path=/scratch_gs/malie102/data/fasttext/dewiki-20170501-3_3-5,fasttext_path=/scratch_gs/malie102/code/fastText/fasttext,iterations=5,min_n=3,max_n=3 train_wikipedia_hilbert.job
qsub -v input_file=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,output_path=/scratch_gs/malie102/data/fasttext/dewiki-20170501-4_4-5,fasttext_path=/scratch_gs/malie102/code/fastText/fasttext,iterations=5,min_n=4,max_n=4 train_wikipedia_hilbert.job
qsub -v input_file=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,output_path=/scratch_gs/malie102/data/fasttext/dewiki-20170501-5_5-5,fasttext_path=/scratch_gs/malie102/code/fastText/fasttext,iterations=5,min_n=5,max_n=5 train_wikipedia_hilbert.job
qsub -v input_file=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,output_path=/scratch_gs/malie102/data/fasttext/dewiki-20170501-6_6-5,fasttext_path=/scratch_gs/malie102/code/fastText/fasttext,iterations=5,min_n=6,max_n=6 train_wikipedia_hilbert.job
qsub -v input_file=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,output_path=/scratch_gs/malie102/data/fasttext/dewiki-20170501-3_6-5,fasttext_path=/scratch_gs/malie102/code/fastText/fasttext,iterations=5,min_n=3,max_n=6 train_wikipedia_hilbert.job

qsub -v input_file=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,output_path=/scratch_gs/malie102/data/fasttext/dewiki-20170501-3_3-10,fasttext_path=/scratch_gs/malie102/code/fastText/fasttext,iterations=10,min_n=3,max_n=3 train_wikipedia_hilbert.job
qsub -v input_file=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,output_path=/scratch_gs/malie102/data/fasttext/dewiki-20170501-4_4-10,fasttext_path=/scratch_gs/malie102/code/fastText/fasttext,iterations=10,min_n=4,max_n=4 train_wikipedia_hilbert.job
qsub -v input_file=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,output_path=/scratch_gs/malie102/data/fasttext/dewiki-20170501-5_5-10,fasttext_path=/scratch_gs/malie102/code/fastText/fasttext,iterations=10,min_n=5,max_n=5 train_wikipedia_hilbert.job
qsub -v input_file=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,output_path=/scratch_gs/malie102/data/fasttext/dewiki-20170501-6_6-10,fasttext_path=/scratch_gs/malie102/code/fastText/fasttext,iterations=10,min_n=6,max_n=6 train_wikipedia_hilbert.job
qsub -v input_file=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,output_path=/scratch_gs/malie102/data/fasttext/dewiki-20170501-3_6-10,fasttext_path=/scratch_gs/malie102/code/fastText/fasttext,iterations=10,min_n=3,max_n=6 train_wikipedia_hilbert.job


qsub -v input_file=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,output_path=/scratch_gs/malie102/data/fasttext/dewiki-20170501-3_3-20,fasttext_path=/scratch_gs/malie102/code/fastText/fasttext,iterations=20,min_n=3,max_n=3 train_wikipedia_hilbert.job
qsub -v input_file=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,output_path=/scratch_gs/malie102/data/fasttext/dewiki-20170501-4_4-20,fasttext_path=/scratch_gs/malie102/code/fastText/fasttext,iterations=20,min_n=4,max_n=4 train_wikipedia_hilbert.job
qsub -v input_file=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,output_path=/scratch_gs/malie102/data/fasttext/dewiki-20170501-5_5-20,fasttext_path=/scratch_gs/malie102/code/fastText/fasttext,iterations=20,min_n=5,max_n=5 train_wikipedia_hilbert.job
qsub -v input_file=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,output_path=/scratch_gs/malie102/data/fasttext/dewiki-20170501-6_6-20,fasttext_path=/scratch_gs/malie102/code/fastText/fasttext,iterations=20,min_n=6,max_n=6 train_wikipedia_hilbert.job
qsub -v input_file=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,output_path=/scratch_gs/malie102/data/fasttext/dewiki-20170501-3_6-20,fasttext_path=/scratch_gs/malie102/code/fastText/fasttext,iterations=20,min_n=3,max_n=6 train_wikipedia_hilbert.job

qsub -v input_file=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,output_path=/scratch_gs/malie102/data/fasttext/dewiki-20170501-3_3-50,fasttext_path=/scratch_gs/malie102/code/fastText/fasttext,iterations=50,min_n=3,max_n=3 train_wikipedia_hilbert.job
qsub -v input_file=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,output_path=/scratch_gs/malie102/data/fasttext/dewiki-20170501-4_4-50,fasttext_path=/scratch_gs/malie102/code/fastText/fasttext,iterations=50,min_n=4,max_n=4 train_wikipedia_hilbert.job
qsub -v input_file=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,output_path=/scratch_gs/malie102/data/fasttext/dewiki-20170501-5_5-50,fasttext_path=/scratch_gs/malie102/code/fastText/fasttext,iterations=50,min_n=5,max_n=5 train_wikipedia_hilbert.job
qsub -v input_file=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,output_path=/scratch_gs/malie102/data/fasttext/dewiki-20170501-6_6-50,fasttext_path=/scratch_gs/malie102/code/fastText/fasttext,iterations=50,min_n=6,max_n=6 train_wikipedia_hilbert.job
qsub -v input_file=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,output_path=/scratch_gs/malie102/data/fasttext/dewiki-20170501-3_6-50,fasttext_path=/scratch_gs/malie102/code/fastText/fasttext,iterations=50,min_n=3,max_n=6 train_wikipedia_hilbert.job

qsub -v input_file=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,output_path=/scratch_gs/malie102/data/fasttext/dewiki-20170501-3_3-100,fasttext_path=/scratch_gs/malie102/code/fastText/fasttext,iterations=100,min_n=3,max_n=3 train_wikipedia_hilbert.job
qsub -v input_file=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,output_path=/scratch_gs/malie102/data/fasttext/dewiki-20170501-4_4-100,fasttext_path=/scratch_gs/malie102/code/fastText/fasttext,iterations=100,min_n=4,max_n=4 train_wikipedia_hilbert.job
qsub -v input_file=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,output_path=/scratch_gs/malie102/data/fasttext/dewiki-20170501-5_5-100,fasttext_path=/scratch_gs/malie102/code/fastText/fasttext,iterations=100,min_n=5,max_n=5 train_wikipedia_hilbert.job
qsub -v input_file=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,output_path=/scratch_gs/malie102/data/fasttext/dewiki-20170501-6_6-100,fasttext_path=/scratch_gs/malie102/code/fastText/fasttext,iterations=100,min_n=6,max_n=6 train_wikipedia_hilbert.job
qsub -v input_file=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501.custom.text,output_path=/scratch_gs/malie102/data/fasttext/dewiki-20170501-3_6-100,fasttext_path=/scratch_gs/malie102/code/fastText/fasttext,iterations=100,min_n=3,max_n=6 train_wikipedia_hilbert.job
```



