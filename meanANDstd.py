import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel files
boys_city_df = pd.read_excel('boyscity.xlsx')
boys_village_df = pd.read_excel('boysvillage.xlsx')
girls_city_df = pd.read_excel('girlscity.xlsx')
girls_village_df = pd.read_excel('girlsvillage.xlsx')

# Add Gender and Region columns for each dataset
boys_city_df['Gender'] = 'Male'
boys_city_df['Region'] = 'City'
boys_village_df['Gender'] = 'Male'
boys_village_df['Region'] = 'Village'
girls_city_df['Gender'] = 'Female'
girls_city_df['Region'] = 'City'
girls_village_df['Gender'] = 'Female'
girls_village_df['Region'] = 'Village'

# Combine all data into a single dataframe
combined_df = pd.concat([boys_city_df, boys_village_df, girls_city_df, girls_village_df])

# Rename columns for easier analysis
combined_df.rename(columns={'STRESS': 'Academic_Stress', 'TOTAL': 'Adjustment'}, inplace=True)

# Calculate the mean and standard deviation for key variables (Adjustment and Academic Stress and MSTOTAL)
mean_std_df = combined_df.groupby(['Gender', 'Region']).agg(
    Adjustment_mean=('Adjustment', 'mean'),
    Adjustment_std=('Adjustment', 'std'),
    Academic_Stress_mean=('Academic_Stress', 'mean'),
    Academic_Stress_std=('Academic_Stress', 'std'),
    MSTOTAL_mean=('MSTOTAL', 'mean'),
    MSTOTAL_std=('MSTOTAL', 'std')
).reset_index()

# Set the plot style
sns.set(style="whitegrid")

# 1. Bar plot for Mean and Standard Deviation: Adjustment by Gender and Region
plt.figure(figsize=(8, 6))
sns.barplot(x='Gender', y='Adjustment_mean', hue='Region', data=mean_std_df,
            capsize=0.1)
plt.title('Mean of Adjustment by Gender and Region')
plt.ylabel('Mean of Adjustment')
plt.xlabel('Gender')
plt.show()

plt.figure(figsize=(8, 6))
sns.barplot(x='Gender', y='Adjustment_std', hue='Region', data=mean_std_df, capsize=0.1)
plt.title('Standard Deviation of Adjustment by Gender and Region')
plt.ylabel('Standard Deviation of Adjustment')
plt.xlabel('Gender')
plt.show()

plt.figure(figsize=(8, 6))
sns.barplot(x='Gender', y='Academic_Stress_mean', hue='Region', data=mean_std_df,
            capsize=0.1)
plt.title('Mean of Academic Stress by Gender and Region')
plt.ylabel('Mean of Adjustment')
plt.xlabel('Gender')
plt.show()

plt.figure(figsize=(8, 6))
sns.barplot(x='Gender', y='Academic_Stress_std', hue='Region', data=mean_std_df, capsize=0.1)
plt.title('Standard Deviation of Academic Stress by Gender and Region')
plt.ylabel('Standard Deviation of Academic Stress')
plt.xlabel('Gender')
plt.show()

plt.figure(figsize=(8, 6))
sns.barplot(x='Gender', y='MSTOTAL_mean', hue='Region', data=mean_std_df,
            capsize=0.1)
plt.title('Mean of MSTOTAL by Gender and Region')
plt.ylabel('Mean of Adjustment')
plt.xlabel('Gender')
plt.show()

plt.figure(figsize=(8, 6))
sns.barplot(x='Gender', y='MSTOTAL_std', hue='Region', data=mean_std_df, capsize=0.1)
plt.title('Standard Deviation of MSTOTAL by Gender and Region')
plt.ylabel('Standard Deviation of MSTOTAL')
plt.xlabel('Gender')
plt.show()
