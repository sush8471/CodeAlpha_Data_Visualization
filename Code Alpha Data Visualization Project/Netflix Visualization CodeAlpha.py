# Netflix Data Visualization – CodeAlpha Internship Task 3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

sns.set_theme(style="whitegrid", palette="pastel")

# Load dataset
df = pd.read_csv("C:/Users/Sushant/Documents/Trae IDE/Internship Project/Code Alpha Data Visualization Project/netflix_cleaned.csv")



# ========= Visualization 1: Top 10 Directors =========
df['director'] = df['director'].fillna("Not Specified")
top_directors = df[df['director'] != "Not Specified"]['director'].value_counts().head(10)

plt.figure(figsize=(10, 6))
ax = sns.barplot(x=top_directors.values, y=top_directors.index, color="skyblue")
plt.title("Top 10 Directors by Number of Titles on Netflix", fontsize=14, fontweight='bold')
plt.xlabel("Number of Titles")
plt.ylabel("Director")
for i, v in enumerate(top_directors.values):
    plt.text(v + 0.5, i, str(v), color='black', va='center', fontweight='bold')
plt.tight_layout()
plt.savefig("top_directors.png")
plt.close()






# ========= Visualization 2: Rating by Type =========
df.dropna(subset=['rating'], inplace=True)
rating_type = df.groupby(['rating', 'type']).size().unstack().fillna(0)
rating_type = rating_type.loc[rating_type.sum(axis=1).sort_values(ascending=False).index]

plt.figure(figsize=(12, 6))
rating_type.plot(kind='bar', width=0.8, colormap='coolwarm', edgecolor='black')
plt.title("Distribution of Content Ratings by Type", fontsize=14, fontweight='bold')
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("rating_by_type.png")
plt.close()







# ========= Visualization 3: Genre Trend Over Years =========
df['year_added'] = pd.to_datetime(df['date_added'], errors='coerce').dt.year
df_genre = df[['listed_in', 'year_added']].dropna()
df_genre['listed_in'] = df_genre['listed_in'].str.split(', ')
df_genre = df_genre.explode('listed_in')

top_genres = df_genre['listed_in'].value_counts().head(5).index
df_top = df_genre[df_genre['listed_in'].isin(top_genres)]
genre_trend = df_top.groupby(['year_added', 'listed_in']).size().reset_index(name='count')

plt.figure(figsize=(12, 6))
sns.lineplot(data=genre_trend, x='year_added', y='count', hue='listed_in', marker="o", palette='tab10')
plt.title("Top 5 Genres Trend Over the Years", fontsize=14, fontweight='bold')
plt.xlabel("Year Added to Netflix")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("genre_trend.png")
plt.close()







# ========= Visualization 4: Movie vs TV Pie Chart =========
type_counts = df['type'].value_counts()
plt.figure(figsize=(6, 6))
colors = ['#ff9999','#66b3ff']
explode = (0.05, 0)

plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140,
        colors=colors, explode=explode, shadow=True, textprops={'fontsize': 12})
plt.title("Netflix Content Share: Movies vs TV Shows", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig("movie_vs_tv_pie.png")
plt.close()
