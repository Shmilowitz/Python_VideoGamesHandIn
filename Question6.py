import numpy as np, matplotlib.pyplot as plt, webget, pandas as pd,collections

vgsales = pd.read_csv('vgsales.csv',quotechar='"',skipinitialspace=True, delimiter=',')
data = vgsales.as_matrix()#Which region has the most sales per person?


# NA
platform_roll_upNA = vgsales.groupby('Platform')['NA_Sales'].sum()
idx_maxNA = platform_roll_upNA.idxmax()
NAmsg = "North America's best selling platform is {} with {} Million sales"
# print("North America\n", NAmsg.format(idx_maxNA, "%.2f" % platform_roll_upNA[idx_maxNA]), "\n")
# EU
platform_roll_upEU = vgsales.groupby('Platform')['EU_Sales'].sum()
idx_maxEU = platform_roll_upEU.idxmax()
EUmsg = "European's best selling platform is {} with {} Million sales"
# print("Europe\n",EUmsg.format(idx_maxEU, "%.2f" % platform_roll_upEU[idx_maxEU]), "\n")
# Japan
platform_roll_upJP = vgsales.groupby('Platform')['JP_Sales'].sum()
idx_maxJP = platform_roll_upJP.idxmax()
JPmsg = "Japan's best selling platform is {} with {} Million sales"
# print("Japan's\n",JPmsg.format(idx_maxJP, "%.2f" % platform_roll_upJP[idx_maxJP]), "\n")


print("Which region has the most sales per person?")
JPpop = 126_135_040
NApop = 362_346_086
EUpop = 506_279_458
print('JP sales per person', platform_roll_upJP[idx_maxJP]*1_000_000 / JPpop)
print('NA sales per person', platform_roll_upNA[idx_maxNA]*1_000_000 / NApop)
print('Euro sales per person', platform_roll_upEU[idx_maxEU]*1_000_000 / EUpop)


objects = [
'Japan','North America','Europe'
]
performance = [
platform_roll_upJP[idx_maxJP]*1_000_000 / JPpop, platform_roll_upNA[idx_maxNA]*1_000_000 / NApop, platform_roll_upEU[idx_maxEU]*1_000_000 / EUpop
]

y_pos = np.arange(len(objects))
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects, rotation=45)
plt.ylabel('Sales per person')
plt.title('Region with most sales per person')
plt.savefig('Question6Chart.png', bbox_inches='tight',dpi=200)
