import numpy as np, matplotlib.pyplot as plt, webget, pandas as pd,collections

vgsales = pd.read_csv('vgsales.csv',quotechar='"',skipinitialspace=True, delimiter=',')
data = vgsales.as_matrix()

#Which game genre is the most popular in 2012?
print("Which game genre is the most popular in 2012?")
mask2012 = (data[:,3] == 2012)
genre2012 = collections.Counter(data[mask2012][:,4])
print(genre2012.most_common(10))

#Plot Generator
objects = [genre2012.most_common(10)[0][0],genre2012.most_common(10)[1][0],
genre2012.most_common(10)[2][0],genre2012.most_common(10)[3][0],
genre2012.most_common(10)[4][0],genre2012.most_common(10)[5][0],genre2012.most_common(10)[6][0],
genre2012.most_common(10)[7][0],genre2012.most_common(10)[8][0],genre2012.most_common(10)[9][0]]

performance = [genre2012.most_common(10)[0][1],genre2012.most_common(10)[1][1],
genre2012.most_common(10)[2][1],genre2012.most_common(10)[3][1],
genre2012.most_common(10)[4][1],genre2012.most_common(10)[5][1],genre2012.most_common(10)[6][1],
genre2012.most_common(10)[7][1],genre2012.most_common(10)[8][1],genre2012.most_common(10)[9][1]]

y_pos = np.arange(len(objects))

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects, rotation=45)
plt.ylabel('Amount of games')
plt.title('Most popular game genre in 2012(Top 10)')
plt.savefig('Plots/Question3Chart.png', bbox_inches='tight')
#Saved version is scaled so everything can be seen properly compared to "show" version
#plt.show()