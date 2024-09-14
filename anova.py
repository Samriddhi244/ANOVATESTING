import pandas
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

filepath1 = "girlsvillage.xlsx"
filepath2 = "girlscity.xlsx"
filepath3 = "boysvillage.xlsx"
filepath4 = "boyscity.xlsx"

girls_village_df = pandas.read_excel(filepath1)
girls_city_df = pandas.read_excel(filepath2)
boys_village_df = pandas.read_excel(filepath3)
boys_city_df = pandas.read_excel(filepath4)

girls_village_df['Gender'] = 'Female'
girls_village_df['Region'] = 'Village'

girls_city_df['Gender'] = 'Female'
girls_city_df['Region'] = 'City'

boys_village_df['Gender'] = 'Male'
boys_village_df['Region'] = 'Village'

boys_city_df['Gender'] = 'Male'
boys_city_df['Region']='City'


combined_df = pandas.concat([boys_city_df, boys_village_df, girls_city_df, girls_village_df])
print(combined_df.head())


combined_df['MS1'].fillna(combined_df['MS1'].median(), inplace=True)

# Check for missing data
missing_data = combined_df.isnull().sum()
print(missing_data)

combined_df.rename(columns={'STRESS': 'Academic_Stress', 'TOTAL': 'Adjustment'}, inplace=True)

# Prepare the formula for factorial ANOVA: Adjustment ~ Academic_Stress * Gender * Region
anova_formula = 'Adjustment ~ Academic_Stress * Gender * Region'

# Fit the model
anova_model = ols(anova_formula, data=combined_df).fit()

# Perform ANOVA
anova_table = sm.stats.anova_lm(anova_model, typ=2)

# Display the ANOVA table
print(anova_table)

# Check if F-value is greater than p-value
for index, row in anova_table.iterrows():
    f_value = row['F']
    p_value = row['PR(>F)']
    if f_value > p_value:
        print(f"{index}: Significant (F-value is greater than p-value)")
    else:
        print(f"{index}: Not Significant (F-value is less than or equal to p-value)")

anova_formula = 'AD1 ~ Academic_Stress * Gender * Region'

# Fit the model
anova_model = ols(anova_formula, data=combined_df).fit()

# Perform ANOVA
anova_table = sm.stats.anova_lm(anova_model, typ=2)

# Display the ANOVA table
print(anova_table)

# Check if F-value is greater than p-value
for index, row in anova_table.iterrows():
    f_value = row['F']
    p_value = row['PR(>F)']
    if f_value > p_value:
        print(f"{index}: Significant (F-value is greater than p-value)")
    else:
        print(f"{index}: Not Significant (F-value is less than or equal to p-value)")

anova_formula = 'AD2 ~ Academic_Stress * Gender * Region'

# Fit the model
anova_model = ols(anova_formula, data=combined_df).fit()

# Perform ANOVA
anova_table = sm.stats.anova_lm(anova_model, typ=2)

# Display the ANOVA table
print(anova_table)

# Check if F-value is greater than p-value
for index, row in anova_table.iterrows():
    f_value = row['F']
    p_value = row['PR(>F)']
    if f_value > p_value:
        print(f"{index}: Significant (F-value is greater than p-value)")
    else:
        print(f"{index}: Not Significant (F-value is less than or equal to p-value)")

anova_formula = 'AD3 ~ Academic_Stress * Gender * Region'

# Fit the model
anova_model = ols(anova_formula, data=combined_df).fit()

# Perform ANOVA
anova_table = sm.stats.anova_lm(anova_model, typ=2)

# Display the ANOVA table
print(anova_table)

# Check if F-value is greater than p-value
for index, row in anova_table.iterrows():
    f_value = row['F']
    p_value = row['PR(>F)']
    if f_value > p_value:
        print(f"{index}: Significant (F-value is greater than p-value)")
    else:
        print(f"{index}: Not Significant (F-value is less than or equal to p-value)")

anova_formula = 'MSTOTAL ~ Academic_Stress * Gender * Region'

# Fit the model
anova_model = ols(anova_formula, data=combined_df).fit()

# Perform ANOVA
anova_table = sm.stats.anova_lm(anova_model, typ=2)

# Display the ANOVA table
print(anova_table)

# Check if F-value is greater than p-value
for index, row in anova_table.iterrows():
    f_value = row['F']
    p_value = row['PR(>F)']
    if f_value > p_value:
        print(f"{index}: Significant (F-value is greater than p-value)")
    else:
        print(f"{index}: Not Significant (F-value is less than or equal to p-value)")

anova_formula = 'MS1 ~ Academic_Stress * Gender * Region'

# Fit the model
anova_model = ols(anova_formula, data=combined_df).fit()

# Perform ANOVA
anova_table = sm.stats.anova_lm(anova_model, typ=2)

# Display the ANOVA table
print(anova_table)

# Check if F-value is greater than p-value
for index, row in anova_table.iterrows():
    f_value = row['F']
    p_value = row['PR(>F)']
    if f_value > p_value:
        print(f"{index}: Significant (F-value is greater than p-value)")
    else:
        print(f"{index}: Not Significant (F-value is less than or equal to p-value)")

anova_formula = 'MS2 ~ Academic_Stress * Gender * Region'

# Fit the model
anova_model = ols(anova_formula, data=combined_df).fit()

# Perform ANOVA
anova_table = sm.stats.anova_lm(anova_model, typ=2)

# Display the ANOVA table
print(anova_table)

# Check if F-value is greater than p-value
for index, row in anova_table.iterrows():
    f_value = row['F']
    p_value = row['PR(>F)']
    if f_value > p_value:
        print(f"{index}: Significant (F-value is greater than p-value)")
    else:
        print(f"{index}: Not Significant (F-value is less than or equal to p-value)")

anova_formula = 'MS3 ~ Academic_Stress * Gender * Region'

# Fit the model
anova_model = ols(anova_formula, data=combined_df).fit()

# Perform ANOVA
anova_table = sm.stats.anova_lm(anova_model, typ=2)

# Display the ANOVA table
print(anova_table)

# Check if F-value is greater than p-value
for index, row in anova_table.iterrows():
    f_value = row['F']
    p_value = row['PR(>F)']
    if f_value > p_value:
        print(f"{index}: Significant (F-value is greater than p-value)")
    else:
        print(f"{index}: Not Significant (F-value is less than or equal to p-value)")

anova_formula = 'MS4 ~ Academic_Stress * Gender * Region'

# Fit the model
anova_model = ols(anova_formula, data=combined_df).fit()

# Perform ANOVA
anova_table = sm.stats.anova_lm(anova_model, typ=2)

# Display the ANOVA table
print(anova_table)

# Check if F-value is greater than p-value
for index, row in anova_table.iterrows():
    f_value = row['F']
    p_value = row['PR(>F)']
    if f_value > p_value:
        print(f"{index}: Significant (F-value is greater than p-value)")
    else:
        print(f"{index}: Not Significant (F-value is less than or equal to p-value)")

anova_formula = 'MS5 ~ Academic_Stress * Gender * Region'

# Fit the model
anova_model = ols(anova_formula, data=combined_df).fit()

# Perform ANOVA
anova_table = sm.stats.anova_lm(anova_model, typ=2)

# Display the ANOVA table
print(anova_table)

# Check if F-value is greater than p-value
for index, row in anova_table.iterrows():
    f_value = row['F']
    p_value = row['PR(>F)']
    if f_value > p_value:
        print(f"{index}: Significant (F-value is greater than p-value)")
    else:
        print(f"{index}: Not Significant (F-value is less than or equal to p-value)")

anova_formula = 'MS6 ~ Academic_Stress * Gender * Region'

# Fit the model
anova_model = ols(anova_formula, data=combined_df).fit()

# Perform ANOVA
anova_table = sm.stats.anova_lm(anova_model, typ=2)

# Display the ANOVA table
print(anova_table)

# Check if F-value is greater than p-value
for index, row in anova_table.iterrows():
    f_value = row['F']
    p_value = row['PR(>F)']
    if f_value > p_value:
        print(f"{index}: Significant (F-value is greater than p-value)")
    else:
        print(f"{index}: Not Significant (F-value is less than or equal to p-value)")