import pandas as pd
from def_readexcel import excelread
from def_PCA import myPCA
from def_BL import BL
from def_DataFlame_plot import plotDataFlame

# ---------xlsxファイルからデータの読み込み---------
df = excelread('pca_data_all.xlsx')  # xlsxの読み込み．#読み込むエクセルファイル名を指定
df_index = list(df.index)            # DataFlameのindexを取得 → PCA()にDataFlameを入れるとndarrayへ変換されるため，個体番号のデータが消えるため．

# ---------読み込んだデータの解析---------
df_BL = BL(df)              # 体長倍に変換
PCA_score = myPCA(df_BL)    # 読み込みデータを標準化して主成分分析
PCA_score = pd.DataFrame(PCA_score,         # PCAで返ってきたndarrayをDataFlameに変換
                         index=df_index,
                         columns=['PC1', 'PC2', 'PC3', 'PC4', 'PC5', 'PC6', 'PC7', 'PC8', 'PC9'])

# ---------データのプロット---------
# plotDataFlame()  # 散布図をプロット
plotDataFlame(PCA_score)  # 散布図をプロット