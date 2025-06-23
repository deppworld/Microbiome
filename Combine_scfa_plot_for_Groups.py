import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

############Conmibe all groupfile in one file##########
# Load each file (they already have 'Time_Point' column)
baseline = pd.read_csv("baseline.csv")
eight_weeks = pd.read_csv("8weeks.csv")
six_months = pd.read_csv("6months.csv")

# Concatenate without adding extra columns
combined = pd.concat([baseline, eight_weeks, six_months], ignore_index=True)

# Save to CSV
combined.to_csv("combined_metabolites.csv", index=False)


######### Plot through combine file###########

# Load and prepare the data
df = pd.read_csv('combined_metabolites.csv')
df = df[['name', 'flux', 'Group', 'timepoint']].dropna()
df = df.rename(columns={'name': 'Metabolite', 'flux': 'Flux', 'Group': 'Group', 'timepoint': 'TimePoint'})
df['TimePoint'] = pd.Categorical(df['TimePoint'], categories=['Baseline', 'EightWeeks', 'SixMonths'], ordered=True)

# Plot with facet by Group
g = sns.catplot(
    data=df, x='Metabolite', y='Flux', hue='TimePoint',
    col='Group', kind='box', height=6, aspect=1.5, palette='Set2'
)
# Rotate x-axis labels and set title
g.set_xticklabels(rotation=90)
g.set_titles("Group: {col_name}")
g.fig.subplots_adjust(top=0.85)
g.fig.suptitle("Metabolite Flux by Group, Time Point, and Metabolite")

# Move legend to upper left
#g._legend.set_bbox_to_anchor((0.01, 0.98))  # Adjusts position: (x, y)
#g._legend.set_loc("upper left")

#or

# Move legend to upper right
g._legend.set_bbox_to_anchor((0.99, 0.98))
g._legend.set_title("TimePoint")  # Optional: Set legend title

plt.tight_layout()
plt.savefig("Groupwise_boxplot.png", bbox_inches='tight', dpi=300)


df['Group_TimePoint'] = df['Group'] + "_" + df['TimePoint'].astype(str)

plt.figure(figsize=(14, 8))
sns.boxplot(data=df, x='Metabolite', y='Flux', hue='Group_TimePoint', dodge=True)
sns.stripplot(data=df, x='Metabolite', y='Flux', hue='Group_TimePoint', dodge=True, jitter=True, alpha=0.5)

plt.title("Metabolite Flux by Group-TimePoint Combination")
plt.ylabel("Flux (Concentration)")
plt.xlabel("Metabolite")
plt.xticks(rotation=90)
plt.legend(title="Group & TimePoint", bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.savefig("Combine_timepoint_box_strip_plot.png", bbox_inches='tight', dpi=300)


