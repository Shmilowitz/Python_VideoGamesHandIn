import numpy as np, matplotlib.pyplot as plt, webget, pandas as pd,collections

vgsales = pd.read_csv('vgsales.csv',quotechar='"',skipinitialspace=True, delimiter=',')
data = vgsales.as_matrix()
#NA
platform_roll_upNA = vgsales.groupby('Platform')['NA_Sales'].sum()
idx_maxNA = platform_roll_upNA.idxmax()
#EU
platform_roll_upEU = vgsales.groupby('Platform')['EU_Sales'].sum()
idx_maxEU = platform_roll_upEU.idxmax()
#Japan
platform_roll_upJP = vgsales.groupby('Platform')['JP_Sales'].sum()
idx_maxJP = platform_roll_upJP.idxmax()

# How big a share of the global sales does the US sales cover?
platform_roll_upTotal = platform_roll_upNA[idx_maxNA] + platform_roll_upEU[idx_maxEU] + platform_roll_upJP[idx_maxJP]
questionMsg2 = "How big a share of the global sales does the US sales cover?\n"
globalMsg = "Global sales is {} \n US sales is {} \n US sales is {}% of the global sales"
globalOne = platform_roll_upTotal / 100
UsVsGlobal = platform_roll_upNA[idx_maxNA] / globalOne
print(questionMsg2, globalMsg.format("%.2f" % platform_roll_upTotal, "%.2f" % platform_roll_upNA[idx_maxNA],"%.2f" % UsVsGlobal ))

#Question 2 - plot generator
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct
labels = 'Japan', 'Europe', 'North America'
sizes = [platform_roll_upJP[idx_maxJP],platform_roll_upEU[idx_maxEU],platform_roll_upNA[idx_maxNA]]
explode = (0, 0,0.1)

fig1, ax1 = plt.subplots()
ax1.pie(sizes,explode=explode, labels=labels, autopct=make_autopct(sizes),shadow=True, startangle=90)
ax1.axis('equal')
plt.title("How big a share of the global sales does the NA sales cover?\n (Numbers are in millions)")
plt.savefig('Plots/Question2Chart.png')
#plt.show()