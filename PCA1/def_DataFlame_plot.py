# DataFlame型の引数のプロット
# ------------- memo -------------
# 引数 : DataFlame
# fig.add_subplot(総行数，総列数，サブプロット番号)

import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')
font = {'family': 'meiryo'}
matplotlib.rc('font', **font)


def plotDataFlame(df):
    x = df.loc[1, 'PC1']
    y = df.loc[1, 'PC2']
    z = df.loc[1, 'PC3']
    print(x)
    print(y)
    print(type(x))
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(x, y, z,  alpha=0.5)
    plt.show()