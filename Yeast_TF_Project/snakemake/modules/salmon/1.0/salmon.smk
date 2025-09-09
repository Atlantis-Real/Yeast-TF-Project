configfile: "config/config.yaml"1

BAM_DIR = config["bam_dir"]

# List all BAM files (remove .bam)
SAMPLES = [
    os.path.splitext(f)[0]
    for f in os.listdir(BAM_DIR)
    if f.endswith(".bam")
]

rule all:
    input:
        expand("data/{sample}/quant.sf", sample=SAMPLES)

rule bam_to_fastq:
    input:
        lambda wildcards: os.path.join(BAM_DIR, f"{wildcards.sample}.bam")
    output:
        temp("data/{sample}.fastq.gz")
    threads: 8
    conda:
        "envs/bedtools.yaml"  
    shell:
        """
        bedtools bamtofastq \
            -i {input} \
            -fq >(gzip -c > {output})
        """

rule salmon_quant_se:
    input:
        fq="data/{sample}.fastq.gz",
        index=config["salmon_index"]
    output:
        "data/{sample}/quant.sf"
    threads: 8
    conda: "envs/salmon.yaml"
    shell: 
        """
        salmon quant \
          -i {input.index} \
          -l A \
          -r {input.fq} \
          -p {threads} \
          --validateMappings \
          -o data/{wildcards.sample}
        """
