import numpy as np, matplotlib.pyplot as plt, webget, pandas as pd,collections, csv

vgsales = pd.read_csv('vgsales.csv',quotechar='"',skipinitialspace=True, delimiter=',')
data = vgsales.as_matrix()#Which region has the most sales per person?


print("Which region has the most sales per person?")
JPpop = 126_135_040
NApop = 362_346_086
EUpop = 506_279_458

csv_file = csv.reader(open("vgsales.csv"))
distEU = 0
for row in csv_file:
    _distEU = row[7]
    try: 
        _distEU = float(_distEU)
    except ValueError:
        _distEU = 0

    distEU += _distEU
csv_file = csv.reader(open("vgsales.csv"))
distNA = 0
for row in csv_file:
    _distNA = row[6]
    try: 
        _distNA = float(_distNA)
    except ValueError:
        _distNA = 0

    distNA += _distNA
csv_file = csv.reader(open("vgsales.csv"))
distJP = 0
for row in csv_file:
    _dist = row[8]
    try: 
        _dist = float(_dist)
    except ValueError:
        _dist = 0

    distJP += _dist

objects = [
'Japan','North America','Europe'
]
performance = [distJP * 1_000_000 / JPpop, distNA * 1_000_000 / NApop, distEU * 1_000_000 / EUpop
]
y_pos = np.arange(len(objects))
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects, rotation=45)
plt.ylabel('Sales per person')
plt.title('Region with most sales per person')
plt.savefig('Question6Chart.png', bbox_inches='tight',dpi=200)
