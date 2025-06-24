import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
flux = pd.read_csv("exchange_fluxes.csv")
annot = pd.read_csv("annotations.csv")
metadata = pd.read_csv("metadata.txt", sep="\t")

# Function to process metabolites
def process_metabolite(metabolite_names, output_prefix):
    # Merge annotations
    df = flux.merge(annot, on="reaction", how="left")

    # Filter for the given metabolite
    df_metabolite = df[df['name'].str.contains('|'.join(metabolite_names), case=False, na=False)]

    # Keep only secreted metabolites (flux > 0)
    df_metabolite = df_metabolite[df_metabolite["flux"] > 0]

    # Save filtered metabolite fluxes to a file
    df_metabolite.to_csv(f"{output_prefix}_filtered_fluxes.csv", index=False, sep="\t")

    # Merge with metadata
    df_merged = df_metabolite.merge(metadata, on="sample_id")
    
    # Save merged data to a file
    df_merged.to_csv(f"{output_prefix}_merged_fluxes_with_metadata.tsv", sep="\t", index=False)
    
    return df_merged

# Process SCFAs
scfa_names = ['acetate', 'propionate', 'butyrate', 'isobutyrate', 'valerate', 'isovalerate']
df_merged_scfa = process_metabolite(scfa_names, "scfa")

# Process Bile Acids
bileacid_names = ['cholate', 'cholanate', 'Ursodiol']
df_merged_bileacid = process_metabolite(bileacid_names, "bileacid")

# Amino Acids
amino_acid_names = [
    'Glycine', 'L-alanine', 'L-argininium', 'L-asparagine', 'L-aspartate',
    'L-cysteine', 'L-glutamate', 'L-glutamine', 'L-histidine', 'L-isoleucine',
    'L-leucine', 'L-lysinium', 'L-methionine', 'L-phenylalanine', 'L-proline',
    'L-serine', 'L-threonine', 'L-tryptophan', 'L-tyrosine', 'L-valine',
    'D-alanine', 'Ornithine', 'L-methionine sulfoxide', 'L-cystine',
    'L-cysteinylglycine', 'Glycylleucine', 'Glycyl-L-aspartate'
]

# Process Amino Acids
df_merged_amino_acids = process_metabolite(amino_acid_names, "amino_acids")

# Vitamins
vitamin_names = [
    'Nicotinate', 'Nicotinamide', 'Pyridoxal', 'Pyridoxamine', 'Pyridoxine',
    'Folate', 'Thiamin', 'Riboflavin', '(R)-Pantothenate', '4-Aminobenzoate'
]

# Process Vitamins
df_merged_vitamins = process_metabolite(vitamin_names, "vitamins")


# Function to plot results
def plot_flux_data(df_merged, metabolite_name):
    # Plot Group-wise Fluxes
    sns.set(style="whitegrid")
    plt.figure(figsize=(16, 8))
    sns.boxplot(data=df_merged, x="Group", y="flux", hue="name")
    sns.stripplot(data=df_merged, x="Group", y="flux", hue="name", dodge=True, color='black', size=3, alpha=0.4)
    plt.title(f"{metabolite_name} Fluxes across Groups")
    plt.ylabel("Flux (mmol/gDW/hr)")
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.,ncol=2, fontsize='small') # ncol=2  This puts the legend in two columns
    plt.tight_layout(rect=[0, 0, 0.85, 1])  # Leave space for the legend
    plt.savefig(f"{metabolite_name.lower()}_flux_groupwise.png", dpi=300)

    # Plot Recruitment-wise Fluxes
    sns.set(style="whitegrid")
    plt.figure(figsize=(16, 8))
    sns.boxplot(data=df_merged, x="Recruitment", y="flux", hue="name")
    sns.stripplot(data=df_merged, x="Recruitment", y="flux", hue="name", dodge=True, color='black', size=3, alpha=0.4)
    plt.title(f"{metabolite_name} Fluxes across Recruitment")
    plt.ylabel("Flux (mmol/gDW/hr)")
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.,ncol=2, fontsize='small') # ncol=2  This puts the legend in two columns
    plt.tight_layout(rect=[0, 0, 0.85, 1])  # Leave space for the legend
    plt.savefig(f"{metabolite_name.lower()}_flux_groupwise_recruitment.png", dpi=300)

    # Option 1: Facet by Recruitment
    sns.set(style="whitegrid")
    g = sns.catplot(
        data=df_merged,
        x="Group", y="flux", hue="name",
        col="Recruitment", # Facet by Recruitment
        kind="box", height=6, aspect=2    # Increase aspect ratio for wider subplots
    )
    g.map_dataframe(sns.stripplot, x="Group", y="flux", hue="name", dodge=True, color='black', size=3, alpha=0.4)
    g.set_axis_labels("Group", "Flux (mmol/gDW/hr)")
    g.set_titles("Recruitment: {col_name}")
    g.tight_layout()
    plt.savefig(f"{metabolite_name.lower()}_flux_by_group_and_recruitment.png", dpi=300)

    # Option 2: Group + Recruitment Combined
    df_merged['Group_Recruitment'] = df_merged['Group'] + "_" + df_merged['Recruitment']
    sns.set(style="whitegrid")
    plt.figure(figsize=(16, 8))
    sns.boxplot(data=df_merged, x="Group_Recruitment", y="flux", hue="name", palette="Set2")
    sns.stripplot(data=df_merged, x="Group_Recruitment", y="flux", hue="name", dodge=True, color='black', size=3, alpha=0.4)
    plt.title(f"{metabolite_name} Fluxes by Group and Recruitment")
    plt.ylabel("Flux (mmol/gDW/hr)")
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.,ncol=2, fontsize='small') # ncol=2  This puts the legend in two columns
    plt.tight_layout(rect=[0, 0, 0.85, 1])  # Leave space for the legend
    plt.savefig(f"{metabolite_name.lower()}_flux_combined_group_recruitment.png", dpi=300)

# Plot results for SCFAs
plot_flux_data(df_merged_scfa, "SCFA")

# Plot results for Bile Acids
plot_flux_data(df_merged_bileacid, "Bile Acid")

# Plot results for Amino Acids
plot_flux_data(df_merged_amino_acids, "Amino Acids")

# Plot results for Vitamins
plot_flux_data(df_merged_vitamins, "Vitamins")