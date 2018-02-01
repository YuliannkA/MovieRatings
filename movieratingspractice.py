import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
plt.rcParams['figure.figsize'] = 8,4

movies = pd.read_csv('C:\Users\Yulia\Desktop\My Data Science\Python\Movie-Ratings.csv')
movies.head()

movies.columns = ['Film', 'Genre', 'CriticsRating', 'AudienceRating', \
                  'BudgetMillions', 'Year']
movies.Film = movies.Film.astype('category')
movies.Genre = movies.Genre.astype('category')
movies.Year = movies.Year.astype('category')

j = sns.jointplot(data=movies, x = 'CriticsRating', y = 'AudienceRating')

k = sns.jointplot(data=movies, x = 'CriticsRating', y = 'AudienceRating', kind='hex')

ml = sns.distplot(movies.CriticsRating, bins=15)

list1=list()
mylabels = list()
for gen in movies.Genre.cat.categories:
    list1.append(movies[movies.Genre == gen].BudgetMillions)
    mylabels.append(gen)
    
h = plt.hist(list1,bins = 15, stacked = True, label = mylabels)
plt.legend()
plt.show()

f,axes = plt.subplots(1,2,figsize=(12,6), sharex = True, sharey = True)
k2 = sns.kdeplot(movies.BudgetMillions, movies.AudienceRating, ax=axes[0])
k3 = sns.kdeplot(movies.BudgetMillions, movies.CriticsRating, ax = axes[1])
k2.set(xlim=(-20,160))

w1=sns.boxplot(data=movies[movies.Genre == 'Drama'], x ='Year', y = 'CriticsRating')

g1 = sns.FacetGrid(movies, row = 'Genre',col = 'Year', hue = 'Genre')
kws = dict(s=50, linewidth = 0.5, edgecolor = 'black')
g1 = g1.map(plt.scatter, 'CriticsRating', 'AudienceRating', **kws)
g1.set(xlim=(0,100), ylim=(0,100))
for ax in g1.axes.flat:
    ax.plot((0,100),(0,100), c='gray', ls='--')
g1.add_legend()


sns.set_style('darkgrid')
f, axes = plt.subplots(2,2, figsize = (15,15))
k2 = sns.kdeplot(movies.BudgetMillions, movies.AudienceRating, shade = True, shade_lowest=True, cmap = 'inferno', ax=axes[0,0])
k2b = sns.kdeplot(movies.BudgetMillions, movies.AudienceRating, cmap = 'cool', ax=axes[0,0])

k3 = sns.kdeplot(movies.BudgetMillions, movies.CriticsRating, ax = axes[0,1])
k2.set(xlim=(-20,160))
k3.set(xlim=(-20,160))
w1=sns.violinplot(data=movies[movies.Genre == 'Drama'], x ='Year', y = 'CriticsRating', ax=axes[1,0])

k1 = sns.kdeplot(movies.CriticsRating, movies.AudienceRating, shade=True, shade_lowest=True, cmap = 'Reds', ax=axes[1,1])
k1b = sns.kdeplot(movies.CriticsRating, movies.AudienceRating, cmap = 'Reds',ax=axes[1,1])
plt.show()

