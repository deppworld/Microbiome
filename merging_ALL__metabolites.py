import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Load data
flux = pd.read_csv("exchange_fluxes.csv")
annot = pd.read_csv("annotations.csv")

#Merge annotations
df = flux.merge(annot, on="reaction", how="left")
df.to_csv("Annotated_fluxes.csv", index=False, sep="\t")

# Merge with metadata
metadata = pd.read_csv("metadata.txt", sep="\t")
df_merged = df.merge(metadata, on="sample_id")
df_merged.to_csv("merged_fluxes_with_metadata.tsv", sep="\t", index=False)


# Plot Group
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))

sns.boxplot(data=df_merged, x="Group", y="flux", hue="name")
sns.stripplot(data=df_merged, x="Group", y="flux", hue="name", dodge=True, color='black', size=3, alpha=0.4)

plt.title("Metabolites Fluxes across Groups")
plt.ylabel("Flux (mmol/gDW/hr)")
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("Metabolites_flux_groupwise.png", dpi=300)

# Plot Recruitment
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))

sns.boxplot(data=df_merged, x="Recruitment", y="flux", hue="name")
sns.stripplot(data=df_merged, x="Recruitment", y="flux", hue="name", dodge=True, color='black', size=3, alpha=0.4)

plt.title("Metabolites Fluxes across Recruitment")
plt.ylabel("Flux (mmol/gDW/hr)")
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("Metabolites_flux_groupwise_Recruitment.png", dpi=300)

#option1  facet by Recruitment
sns.set(style="whitegrid")

g = sns.catplot(
data=df_merged,
x="Group", y="flux", hue="name",
col="Recruitment", # ➜ facet by Recruitment
kind="box", height=5, aspect=1.2
)
g.map_dataframe(sns.stripplot, x="Group", y="flux", hue="name", dodge=True, color='black', size=3, alpha=0.4)

g.set_axis_labels("Group", "Flux (mmol/gDW/hr)")
g.set_titles("Recruitment: {col_name}")
g.tight_layout()
plt.savefig("Metabolites_flux_by_group_and_recruitment.png", dpi=300)


#option2: Group + Recruitment combined

df_merged['Group_Recruitment'] = df_merged['Group'] + "_" + df_merged['Recruitment']

sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))

sns.boxplot(data=df_merged, x="Group_Recruitment", y="flux", hue="name", palette="Set2")
sns.stripplot(data=df_merged, x="Group_Recruitment", y="flux", hue="name", dodge=True, color='black', size=3, alpha=0.4)

plt.title("Metabolites Fluxes by Group and Recruitment")
plt.ylabel("Flux (mmol/gDW/hr)")
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Metabolites")
plt.tight_layout()
plt.savefig("Metabolites_flux_combined_group_recruitment.png", dpi=300)

