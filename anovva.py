import pandas
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
from statsmodels.stats.anova import anova_lm
import seaborn as sns

# Load data (example paths)
filepath1 = "girlsvillage.xlsx"
filepath2 = "girlscity.xlsx"
filepath3 = "boysvillage.xlsx"
filepath4 = "boyscity.xlsx"

girls_village_df = pandas.read_excel(filepath1)
girls_city_df = pandas.read_excel(filepath2)
boys_village_df = pandas.read_excel(filepath3)
boys_city_df = pandas.read_excel(filepath4)

# Add Gender and Region columns
girls_village_df['Gender'] = 'Female'
girls_village_df['Region'] = 'Village'
girls_city_df['Gender'] = 'Female'
girls_city_df['Region'] = 'City'
boys_village_df['Gender'] = 'Male'
boys_village_df['Region'] = 'Village'
boys_city_df['Gender'] = 'Male'
boys_city_df['Region'] = 'City'

combined_df = pandas.concat([boys_city_df, boys_village_df, girls_city_df, girls_village_df])
combined_df['MS1'].fillna(combined_df['MS1'].median(), inplace=True)

combined_df.rename(columns={'STRESS': 'Academic_Stress', 'TOTAL': 'Adjustment'}, inplace=True)

# Define significance level (alpha)
alpha = 0.05  # You can adjust this to 0.1 for a 10% significance level

# List of dependent variables
dependent_vars = ['Adjustment', 'AD1', 'AD2', 'AD3', 'MSTOTAL', 'MS1', 'MS2', 'MS3', 'MS4', 'MS5', 'MS6']

# Perform ANOVA for each dependent variable and calculate error
for dep_var in dependent_vars:
    anova_formula = f'{dep_var} ~ Academic_Stress * Gender * Region'
    
    # Fit the model
    anova_model = ols(anova_formula, data=combined_df).fit()
    
    # Perform ANOVA
    anova_table = sm.stats.anova_lm(anova_model, typ=2)
    
    # Display the ANOVA table
    print(f"\nANOVA for {dep_var}")
    print(anova_table)
    
    # Extract error values (Residual row)
    residual_row = anova_table.loc['Residual']
    ss_residual = residual_row['sum_sq']
    df_residual = residual_row['df']
    mse = ss_residual / df_residual
    
    # Display error values
    print(f"SS Residual (Error): {ss_residual}")
    print(f"df Residual: {df_residual}")
    print(f"MSE (Mean Squared Error): {mse}")
    
    # Check if p-value is less than the significance level (alpha)
    for index, row in anova_table.iterrows():
        p_value = row['PR(>F)']
        if p_value < alpha:
            print(f"{index}: Significant (p-value < {alpha})")
        else:
            print(f"{index}: Not Significant (p-value >= {alpha})")

   