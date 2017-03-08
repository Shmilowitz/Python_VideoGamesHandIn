import numpy as np, matplotlib.pyplot as plt, webget, pandas as pd,collections
# import  Question3, Question4, Question2
#WEBGET ONLY USE ONCE TO DONWLOAD VGSALES.CSV
#webget.download('https://raw.githubusercontent.com/DaMexicanJustice/frantic_midnight/master/data%20sets/vgsales.csv')
vgsales = pd.read_csv('vgsales.csv',quotechar='"',skipinitialspace=True, delimiter=',')
data = vgsales.as_matrix()

#Which platform is the most popular in the regions NA, EU and Japan?
# print("Which platform is the most popular in the regions NA, EU and Japan?")
# NA
platform_roll_upNA = vgsales.groupby('Platform')['NA_Sales'].sum()
idx_maxNA = platform_roll_upNA.idxmax()
NAmsg = "North America's best selling platform is {} with {} Million sales"
print("North America\n", NAmsg.format(idx_maxNA, "%.2f" % platform_roll_upNA[idx_maxNA]), "\n")
#EU
platform_roll_upEU = vgsales.groupby('Platform')['EU_Sales'].sum()
idx_maxEU = platform_roll_upEU.idxmax()
EUmsg = "European's best selling platform is {} with {} Million sales"
print("Europe\n",EUmsg.format(idx_maxEU, "%.2f" % platform_roll_upEU[idx_maxEU]), "\n")
#Japan
platform_roll_upJP = vgsales.groupby('Platform')['JP_Sales'].sum()
idx_maxJP = platform_roll_upJP.idxmax()
JPmsg = "Japan's best selling platform is {} with {} Million sales"
print("Japan's\n",JPmsg.format(idx_maxJP, "%.2f" % platform_roll_upJP[idx_maxJP]), "\n")

objects = [
'Japan= ' + idx_maxJP,'North America= ' + idx_maxNA,'Europe= ' + idx_maxEU
]
performance = [
platform_roll_upJP[idx_maxJP], platform_roll_upNA[idx_maxNA], platform_roll_upEU[idx_maxEU]
]

y_pos = np.arange(len(objects))
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects, rotation=45)
plt.ylabel('Numbers of games sold for popular platform')
plt.title('Most popular platform in all regions\n(Numbers are in millions)')
plt.savefig('Question1Chart.png', bbox_inches='tight',dpi=200)
