This Projects workflow is built around Salmon.

Inserting your desired yeast mrna BAM files and reference cDNA FASTA, the included snakemake pipeline will generate a salmon index and quant.sf files. Expression 
values are then filtered using a curated list of yeast transcription factors (TFs) (https://amigo.geneontology.org/amigo/search/annotation?q=GO:0003700). 

Transcript Per Million (TPM) counts are summarized across samples, and barplots of TF expression are generated and saved as PDF files.
