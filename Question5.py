import numpy as np, matplotlib.pyplot as plt, webget, pandas as pd,collections

vgsales = pd.read_csv('vgsales.csv',quotechar='"',skipinitialspace=True, delimiter=',')
data = vgsales.as_matrix()

#Which year had the most titles released?
print("Which year had the most titles released?")
mostReleased = collections.Counter(data[:,3])
print(mostReleased.most_common(20))

objects = [
mostReleased.most_common(20)[0][0],mostReleased.most_common(20)[1][0],mostReleased.most_common(20)[2][0],
mostReleased.most_common(20)[3][0],mostReleased.most_common(20)[4][0],mostReleased.most_common(20)[5][0],
mostReleased.most_common(20)[6][0],mostReleased.most_common(20)[7][0],mostReleased.most_common(20)[8][0],
mostReleased.most_common(20)[9][0],mostReleased.most_common(20)[10][0],mostReleased.most_common(20)[11][0],
mostReleased.most_common(20)[12][0],mostReleased.most_common(20)[13][0],mostReleased.most_common(20)[14][0],
mostReleased.most_common(20)[15][0],mostReleased.most_common(20)[16][0],mostReleased.most_common(20)[17][0],
mostReleased.most_common(20)[18][0],mostReleased.most_common(20)[19][0]
]

performance = [
mostReleased.most_common(20)[0][1],mostReleased.most_common(20)[1][1],mostReleased.most_common(20)[2][1],
mostReleased.most_common(20)[3][1],mostReleased.most_common(20)[4][1],mostReleased.most_common(20)[5][1],
mostReleased.most_common(20)[6][1],mostReleased.most_common(20)[7][1],mostReleased.most_common(20)[8][1],
mostReleased.most_common(20)[9][1],mostReleased.most_common(20)[10][1],mostReleased.most_common(20)[11][1],
mostReleased.most_common(20)[12][1],mostReleased.most_common(20)[13][1],mostReleased.most_common(20)[14][1],
mostReleased.most_common(20)[15][1],mostReleased.most_common(20)[16][1],mostReleased.most_common(20)[17][1],
mostReleased.most_common(20)[18][1],mostReleased.most_common(20)[19][1]
]

y_pos = np.arange(len(objects))
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects, rotation=90)
plt.ylabel('Amount of games')
plt.title('Most popular publisher in top 200')
plt.savefig('Question5Chart.png', bbox_inches='tight',dpi=200)
#Saved version is scaled so everything can be seen properly compared to "show" version
#plt.show()
print(mostReleased.most_common(20))