import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns

# Load all four datasets
girls_village_df = pd.read_excel('girlsvillage.xlsx')
girls_city_df = pd.read_excel('girlscity.xlsx')
boys_village_df = pd.read_excel('boysvillage.xlsx')
boys_city_df = pd.read_excel('boyscity.xlsx')

# Add Gender and Region columns
girls_village_df['Gender'] = 'Female'
girls_village_df['Region'] = 'Village'
girls_city_df['Gender'] = 'Female'
girls_city_df['Region'] = 'City'
boys_village_df['Gender'] = 'Male'
boys_village_df['Region'] = 'Village'
boys_city_df['Gender'] = 'Male'
boys_city_df['Region'] = 'City'

# Combine all data into one DataFrame
combined_df = pd.concat([boys_city_df, boys_village_df, girls_city_df, girls_village_df])

# Fill missing data in MS1
combined_df['MS1'].fillna(combined_df['MS1'].median(), inplace=True)

# Rename columns for consistency
combined_df.rename(columns={'STRESS': 'Academic_Stress', 'TOTAL': 'Adjustment'}, inplace=True)

# List of dependent variables to run ANOVA on
dependent_vars = ['Adjustment', 'AD1', 'AD2', 'AD3', 'MSTOTAL', 'MS1', 'MS2', 'MS3', 'MS4', 'MS5', 'MS6']

# Create line plots and perform ANOVA for each dependent variable
for dep_var in dependent_vars:
    # Prepare the formula for factorial ANOVA
    anova_formula = f'{dep_var} ~ Academic_Stress * Gender * Region'
    
    # Fit the model
    anova_model = ols(anova_formula, data=combined_df).fit()
    
    # Perform ANOVA
    anova_table = sm.stats.anova_lm(anova_model, typ=2)
    
    # Display the ANOVA table
    print(f"\nANOVA for {dep_var}")
    print(anova_table)
    
    # Check if F-value is greater than p-value
    for index, row in anova_table.iterrows():
        f_value = row['F']
        p_value = row['PR(>F)']
        if f_value > p_value:
            print(f"{index}: Significant (F-value is greater than p-value)")
        else:
            print(f"{index}: Not Significant (F-value is less than or equal to p-value)")

    # Create line plot for the dependent variable
    plt.figure(figsize=(10, 6))
    
    # Use seaborn's lineplot for better visualizations
    sns.lineplot(x='Academic_Stress', y=dep_var, hue='Gender', style='Region', markers=True, data=combined_df)
    
    plt.title(f"Line Plot of {dep_var} vs Academic Stress (by Gender and Region)")
    plt.xlabel("Academic Stress")
    plt.ylabel(dep_var)
    plt.legend(title='Group')
    
    # Display the plot
    plt.show()
