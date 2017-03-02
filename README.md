# metagenome_quicklooks
This is a bash script that has 10 positions This is the main script: QUICKLOOKS_PIPELINE.sh

Software dependencies

bowtie2

prodigal

usearch

Additional script dependencies: perl_quicklook1.pl

contig_stats.pl

make_contig_cov_file.py

pullseq.py

add_missing_annotations.py

These scripts need to be placed in the same directory you are working in or be executable from a root directory. Alternatively you can alter the QUICKLOOKS_PIPELINE.sh script to call to the scripts where you have placed them on your machine.

Run this command as follows:

bash QUICKLOOKS_PIPELINE scaffold.fa forward.reads.fastq reverse.reads.fastq min.length.of.contigs. Job.id BOWTIE email NA threads 0.0001

$1 = path to scaffold.fa file Ex ../scaffold.fa

-this could be a degapped scaffold file such as 100_percent_scaffold_degap

$2 = path to forward reads Ex ../../R1_All_trimmed.fastq or NA if NO_BOWTIE

$3 = path to reverse reads Ex: ../../R2_All_trimmed.fastq or NA if NO_BOWTIE

$4 = min length of cotigs Ex: 1000

$5 = Job ID Ex: F02_w

-can be anything (no spaces) just added to front of scaffold as an id

-ex: F02_4_scafold_67 or F_0_@_scaffold_67

$6 = BOWTIE or NO_BOWTIE

 note if NO_BOWTIE is used then $2 and $3 can say NA because these files are not used
$7 = email or NO_EMAIL

$8 = NA if BOWTIE or if NO_BOWTIE and you dont want contig stats

 or path to Contig_coverage_score_100_Final_paired.txt (file with stats) when NO_BOWTIE 
$9 = number of threads

$10 = evalue default should be 0.0001
