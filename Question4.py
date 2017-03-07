import numpy as np, matplotlib.pyplot as plt, webget, pandas as pd,collections

vgsales = pd.read_csv('vgsales.csv',quotechar='"',skipinitialspace=True, delimiter=',')
data = vgsales.as_matrix()

#Which publisher has the most titles in top 100?
print("Which publisher has the most titles in top 100?")
first100 = (data[:,0]< 101)
pub100 = collections.Counter(data[first100][:,5])
print(pub100.most_common(10))

objects = [pub100.most_common(10)[0][0],pub100.most_common(10)[1][0],
pub100.most_common(10)[2][0],pub100.most_common(10)[3][0],
pub100.most_common(10)[4][0],pub100.most_common(10)[5][0],pub100.most_common(10)[6][0],
pub100.most_common(10)[7][0],pub100.most_common(10)[8][0],pub100.most_common(10)[9][0]]

performance = [pub100.most_common(10)[0][1],pub100.most_common(10)[1][1],
pub100.most_common(10)[2][1],pub100.most_common(10)[3][1],
pub100.most_common(10)[4][1],pub100.most_common(10)[5][1],pub100.most_common(10)[6][1],
pub100.most_common(10)[7][1],pub100.most_common(10)[8][1],pub100.most_common(10)[9][1]]

y_pos = np.arange(len(objects))
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects, rotation=90)
plt.ylabel('Amount of games')
plt.title('Most popular publisher in top 100')
plt.savefig('Question4Chart.png', bbox_inches='tight',dpi=100)
#Saved version is scaled so everything can be seen properly compared to "show" version
#plt.show()
print(pub100.most_common(10))

