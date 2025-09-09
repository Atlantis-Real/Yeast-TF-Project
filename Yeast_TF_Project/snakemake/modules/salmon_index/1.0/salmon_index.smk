configfile: "config/config.yaml"

FA_DIR = config["fa_dir"]

rule all:
    input:
        config["salmon_index"]

rule salmon_index:
    input:
        fasta=FA_DIR
    output:
        directory(config["salmon_index"])
    threads: 8
    conda:
        "envs/salmon.yaml"
    shell:
        """
        salmon index \
            -t {input.fasta} \
            -i {output} \
            -k {config[kmer_size]} \
            -p {threads}
        """

