import pandas
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

filepath1 = "girls village.xlsx"
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

combined_df.rename(columns={'STRESS': 'Academic_Stress', 'TOTAL': 'Adjustment'}, inplace=True)

# Prepare the formula for factorial ANOVA: Adjustment ~ Academic_Stress * Gender * Region
anova_formula = 'Adjustment ~ C(Region)'

# Fit the model
anova_model = ols(anova_formula, data=combined_df).fit()

# Perform ANOVA
anova_table = sm.stats.anova_lm(anova_model, typ=2)

# Display the ANOVA table
print(anova_table)
