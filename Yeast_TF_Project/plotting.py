import numpy as np
import pandas as pd
import os
import glob
import matplotlib.pyplot as plt


# Find all Salmon TF quant files
files = sorted(glob.glob("/Yeast_TF_Project/data/*_quant_TF_only.sf"))

# Store them in a dictionary
samples = {}

for f in files:
    name = os.path.basename(f).replace("_quant_TF_only.sf", "")  # e.g. ERR9593591
    df = pd.read_csv(f, sep="\t")
    samples[name] = df
    print(f"Loaded {name} with {df.shape[0]} rows")

    # Loaded ERR9593591 with 7 rows
    # Loaded ERR9593593 with 7 rows
    # Loaded ERR9593599 with 7 rows
    # Loaded ERR9593602 with 7 rows
    # Loaded ERR9593606 with 7 rows

# Example: access one
# print(samples["ERR9593591"])

# Combine into one DataFrame for plotting
dfs = []
for name, df in samples.items():
    sub = df[["gene", "TPM"]].copy()
    sub.rename(columns={"TPM": name}, inplace=True)
    dfs.append(sub)

merged = dfs[0]
for df in dfs[1:]:
    merged = merged.merge(df, on="gene", how="outer")

# Set up bar positions
tf_names = merged["gene"].values
sample_names = merged.columns[1:]  
x = np.arange(len(tf_names))
width = 0.8 / len(sample_names) 

fig, ax = plt.subplots(figsize=(14, 6))
for i, sample in enumerate(sample_names):
    ax.bar(x + i * width, merged[sample], width, label=sample)

# Barplot of TPM values for each TF in each sample
ax.set_title("Yeast TF TPM Values")
ax.set_xlabel("TF Genes")
ax.set_ylabel("TPM")
ax.set_xticks(x + width * (len(sample_names) - 1) / 2)
ax.set_xticklabels(tf_names, rotation=90)

ax.legend(
    title="Samples",
    loc="upper right",
    bbox_to_anchor=(1, -0.3),  
    ncol=len(sample_names) // 2 or 1, 
    frameon=False
)

plt.tight_layout()

# Save as PDF
outdir = "/Yeast_TF_Project/plot"
os.makedirs(outdir, exist_ok=True)
outfile = os.path.join(outdir, "yeast_TF_TPM_barplot.pdf")
plt.savefig(outfile)

print(f"Saved plot to {outfile}")