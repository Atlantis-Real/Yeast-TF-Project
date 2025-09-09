import pandas as pd


# load TF gene list
df = pd.read_csv(
    "Yeast_TF_Project/data/yeast_TF_list.tsv",
    sep="\t",
    header=None,
    names=["source", "gene", "evidence"]
)


# Get gene symbols 
tf_genes = df["gene"].unique()   

pd.Series(tf_genes).to_csv("Yeast_TF_Project/data/yeast_TF_genes.txt", index=False, header=False)


# Load TF genes
tf_genes = pd.read_csv(
    "/home/lklossok/Morin_Lab/Yeast_TF_Project/data/yeast_TF_genes.txt",
    header=None,
    names=["gene"]
)


# Load quant.sf

# Example quant.sf files:
# Yeast_TF_Project/snakemake/modules/salmon/1.0/data/ERR9593591/quant.sf
# Yeast_TF_Project/snakemake/modules/salmon/1.0/data/ERR9593593/quant.sf
# Yeast_TF_Project/snakemake/modules/salmon/1.0/data/ERR9593599/quant.sf
# Yeast_TF_Project/snakemake/modules/salmon/1.0/data/ERR9593602/quant.sf
# Yeast_TF_Project/snakemake/modules/salmon/1.0/data/ERR9593606/quant.sf

quant = pd.read_csv(
    "/home/lklossok/Morin_Lab/Yeast_TF_Project/snakemake/modules/salmon/1.0/data/ERR9593606/quant.sf",
    sep="\t"
)


# Strip transcript suffix to get gene IDs
quant["gene"] = quant["Name"].str.split("_").str[0]


# Filter quant for TF genes
filtered = quant[quant["gene"].isin(tf_genes["gene"])]


# Save filtered quant
filtered.to_csv(
    "/home/lklossok/Morin_Lab/Yeast_TF_Project/data/ERR9593606_quant_TF_only.sf",
    sep="\t",
    index=False
)
 