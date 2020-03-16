import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set_style('darkgrid')
sns.set_palette('Blues_d')

df = pd.read_csv('World_Happiness_2015_2017.csv')

def filter_year(df, year):
    df = df[df['Year'] == year].nlargest(5, 'Happiness Score')
    return df

df_2015 = filter_year(df, 2015)
df_2016 = filter_year(df, 2016)
df_2017 = filter_year(df, 2017)

# df_final = pd.Dataframe()

df_final = df_2015.append(df_2016, ignore_index=True)
df_final = df_final.append(df_2017, ignore_index=True)
# print(df_final)


# df = df.groupby(['Country'])
# pal=sns.color_palette('Blues_d', len(df_final))

# sns.scatterplot(x='Happiness Score', y='Generosity', hue='Country', data=df_final)

# plt.savefig('image.png')
# print(df.head(15))

sns.barplot(x='Country', y='Generosity', hue='Year', data=df_final)

plt.savefig('image.png')
