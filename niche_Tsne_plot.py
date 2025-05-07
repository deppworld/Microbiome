

#####t-SNE plot for MICOM Niche plot#######


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- USER INPUTS ---
tsne_file = "exported_niche/tsne.csv"  # Path to exported t-SNE file
metadata_file = "exported_niche/metadata.txt"      # Your sample metadata file
group_column = "Group"                     # Metadata column to color by (e.g., Group, Condition, etc.)

# --- LOAD DATA ---
tsne = pd.read_csv(tsne_file, sep=',')
metadata = pd.read_csv(metadata_file, sep='\t')

# --- STRIP WHITESPACE FROM COLUMN NAMES ---
tsne.columns = tsne.columns.str.strip()
metadata.columns = metadata.columns.str.strip()
# --- MERGE ---
merged = pd.merge(tsne, metadata, on='sample_id')
# --- PLOT ---
plt.figure(figsize=(8,6))
sns.scatterplot(data=merged, x='TSNE-1', y='TSNE-2', hue=group_column, style=group_column, s=80)    # For change in colour use "palette='Set2'," # Options: 'Set1', 'Set2', 'pastel', 'dark', 'muted', etc.
plt.title(f"t-SNE Plot Colored by {group_column}")
plt.xlabel("t-SNE 1")
plt.ylabel("t-SNE 2")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("tsne_plot_Group.png", dpi=300, bbox_inches='tight')





# Filter for Respo group
filtered = merged[merged[group_column] == "Respo"]

# Plot
plt.figure(figsize=(8,6))
sns.scatterplot(data=filtered, x='TSNE-1', y='TSNE-2', hue=group_column, style=group_column, s=80)
plt.title(f"t-SNE Plot for Group: Respo")
plt.xlabel("t-SNE 1")
plt.ylabel("t-SNE 2")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("tsne_respo_only.png", dpi=300)


# Filter for Non-Res group
filtered = merged[merged[group_column] == "Non-Res"]

# Plot
plt.figure(figsize=(8,6))
sns.scatterplot(data=filtered, x='TSNE-1', y='TSNE-2', hue=group_column, style=group_column, s=80)
plt.title(f"t-SNE Plot for Group: Respo")
plt.xlabel("t-SNE 1")
plt.ylabel("t-SNE 2")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("tsne_Non-Respo_only.png", dpi=300)

group_column = "Recruitment"                     # Metadata column to color by (e.g., Group, Condition, etc.)

plt.figure(figsize=(8,6))
sns.scatterplot(data=merged, x='TSNE-1', y='TSNE-2', hue=group_column, style=group_column, s=80)
plt.title(f"t-SNE Plot Colored by {group_column}")
plt.xlabel("t-SNE 1")
plt.ylabel("t-SNE 2")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("tsne_plot_Recruitment.png", dpi=300, bbox_inches='tight')


# Filter for Baseline Recruitment
filtered = merged[merged[group_column] == "Baseline"]

# Plot
plt.figure(figsize=(8,6))
sns.scatterplot(data=filtered, x='TSNE-1', y='TSNE-2', hue=group_column, style=group_column, s=80)
plt.title(f"t-SNE Plot for Baseline")
plt.xlabel("t-SNE 1")
plt.ylabel("t-SNE 2")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("tsne_Baseline_only.png", dpi=300)


# Filter for Returned Recruitment
filtered = merged[merged[group_column] == "Returned"]

# Plot
plt.figure(figsize=(8,6))
sns.scatterplot(data=filtered, x='TSNE-1', y='TSNE-2', hue=group_column, style=group_column, s=80)
plt.title(f"t-SNE Plot for Returned")
plt.xlabel("t-SNE 1")
plt.ylabel("t-SNE 2")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("tsne_Returned_only.png", dpi=300)


 #t-SNE plot by mapping one to color(Group) and the other to marker style (Recruitment)
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=merged,
    x='TSNE-1',
    y='TSNE-2',
    hue='Group',           # Color by Group (Respo, Non-Resp)
    style='Recruitment',   # Marker style by Recruitment (Baseline, returned)
    palette='Set2',
s=80
)

plt.title("t-SNE Plot Colored by Group and Shaped by Recruitment")
plt.xlabel("t-SNE 1")
plt.ylabel("t-SNE 2")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("tsne_group_recruitment_combine.png", dpi=300)








