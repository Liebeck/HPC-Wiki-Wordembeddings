# Create a vocabulary and tfidf files
``` bash
 qsub -v input_path=/scratch_gs/malie102/data/wikipedia-de/dewiki-20170501-pages-meta-current.xml.bz2,output_path=/scratch_gs/malie102/data/lda/wikipedia/ process_dump_hilbert.job
```

# Train LDA based on Wikipedia
``` bash
qsub -v k=100 train_lda_hilbert.job
qsub -v k=150 train_lda_hilbert.job
qsub -v k=200 train_lda_hilbert.job
qsub -v k=250 train_lda_hilbert.job
qsub -v k=300 train_lda_hilbert.job
```

