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

plt.figure(figsize=(10,6))

# 1. Main Effect: Gender vs Adjustment
sns.barplot(x='Gender', y='Adjustment',width=0.3, data=combined_df)
plt.title("effect of gender on adjustment")
plt.xlabel("gender")
plt.ylabel("adjustment")
plt.show()

# 2. Main Effect: Region vs Adjustment
sns.barplot(x='Region', y='Adjustment',width=0.4, data=combined_df)
plt.title('Effect of Region on Adjustment')
plt.xlabel("region")
plt.ylabel("adjustment")
plt.show()

# 3. Main Effect: Academic Stress vs Adjustment
sns.lineplot(x='Academic_Stress', y='Adjustment', data=combined_df)
plt.title('Effect of Academic Stress on Adjustment')
plt.xlabel("Academic_Stress")
plt.ylabel("adjustment")
plt.show()

# 4. Main Effect: Mental Stress vs Adjustment
sns.scatterplot(x='MSTOTAL', y='Adjustment', data=combined_df)
sns.lineplot(x='MSTOTAL', y='Adjustment', data=combined_df)
plt.title('Effect of Mental Stress on Adjustment')
plt.xlabel("Mental_Stress")
plt.ylabel("adjustment")
plt.show()

# 4. Interaction Effect: Gender x Region on Adjustment
sns.pointplot(x='Region', y='Adjustment', hue='Gender', data=combined_df)
plt.title('Interaction of Gender and Region on Adjustment')

# 5. Interaction Effect: Academic Stress x Gender on Adjustment
sns.lmplot(x='Academic_Stress', y='Adjustment', hue='Gender', data=combined_df, aspect=1.5)
plt.title('Interaction of Academic Stress and Gender on Adjustment')

# 6. Interaction Effect: Academic Stress x Region on Adjustment
sns.lmplot(x='Academic_Stress', y='Adjustment', hue='Region', data=combined_df, aspect=1.5)
plt.title('Interaction of Academic Stress and Region on Adjustment')

# Adjust the layout
plt.tight_layout()
